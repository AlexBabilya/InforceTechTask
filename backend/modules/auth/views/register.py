from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from modules.role.models import Role
from modules.user.models import User
from modules.user.serializers import UserSerializer


class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        req = request.data
        
        #user_group, _ = Group.objects.get_or_create(name=req.get('role'))
        role_group, _ = Role.objects.get_or_create(name=req.get('role'))

        serializer = UserSerializer(data=req)
         
        if serializer.is_valid():
            try:
                new_user = User.objects.create(
                    username=req.get('email'),
                    email=req.get('email'),
                    first_name=req.get('first_name').capitalize(),
                    last_name=req.get('last_name').capitalize(),
                    is_active=True,
                    phone=req.get('phone'),
                    identification_no=req.get('identification_no'),
                    is_staff=True

                )

                new_user.roles.add(role_group)
                #new_user.groups.add(user_group)

                password = User.objects.make_random_password(length=10)
                new_user.set_password(password)
                new_user.save()

                user = UserSerializer(new_user)
               
                res = {
                    "msg": f"Successfully registered.",
                    "data": user.data,
                    "success": True}
                return Response(data=res, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                res = {
                    "msg": str(e), 
                    "data": None, 
                    "success": False
                }
                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
            
        res = {
            "msg": str(serializer.errors), 
            "data": None, 
            "success": False
        }
        
        return Response(data=res, status=status.HTTP_400_BAD_REQUEST)