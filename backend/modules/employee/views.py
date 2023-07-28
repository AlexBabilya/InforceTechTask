from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from modules.auth.handlers import jwt_decode_handler
from modules.user.models import User
from modules.user.serializers import UserSerializer

from modules.role.models import Role
from .serializers import EmployeeSerializer
from .models import Employee


class CreateEmployeeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        req = request.data

        user = jwt_decode_handler(request.auth).get("username")
        employee_no = req.get("employee_no")
        employee = Employee.objects.filter(Q(employee_no=employee_no))

        if employee.exists():
            res = {
                "msg": f"Employee NO { employee_no } already exists",
                "data": None,
                "success": False,
            }
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

        role_group, _ = Role.objects.get_or_create(name=req.get("employee"))

        serializer = EmployeeSerializer(data=req)

        if serializer.is_valid():
            try:
                new_user = User.objects.create(
                    username=req.get("email"),
                    email=req.get("email"),
                    first_name=req.get("first_name").capitalize(),
                    last_name=req.get("last_name").capitalize(),
                    is_active=True,
                    phone=req.get("phone"),
                    identification_no=req.get("identification_no"),
                    is_staff=True,
                    created_by=user,
                )

                new_user.roles.add(role_group)

                password = User.objects.make_random_password(length=10)
                new_user.set_password(password)
                new_user.save()

                Employee.objects.create(
                    user=new_user, employee_no=req.get("employee_no"), created_by=user
                )

                serializer = UserSerializer(new_user)

                res = {
                    "msg": "Employee successfully created.",
                    "data": serializer.data,
                    "success": True,
                }

                return Response(data=res, status=status.HTTP_201_CREATED)

            except Exception as e:
                res = {"msg": str(e), "data": None, "success": False}

                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

        res = {"msg": str(serializer.errors), "data": None, "success": False}

        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
