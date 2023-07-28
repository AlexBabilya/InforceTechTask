from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from modules.abstract.viewsets import AbstractViewSet
from modules.user.models import User
from modules.role.models import Role
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(AbstractViewSet):
    http_method_names = ('post')
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    
    def create(self, request, *args, **kwargs):
        req = request.data
        employee_no = req.get('employee_no')
        employee = Employee.objects.filter(
            Q(employee_no=employee_no)
        )

        if employee.exists():
            return Response({
                "detail": f"Employee NO { employee_no } already exists",
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        Employee.objects.create(
            user=user,
            employee_no=req.get('employee_no'),
            created_by=request.user.username
        )

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "access": res["access"],
            },
            status=status.HTTP_201_CREATED,
        )
            