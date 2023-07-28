from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from modules.user.models import User
from modules.auth.serializers import UserLoginSerializer
from ..handlers import jwt_payload_handler, jwt_encode_handler


class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, format=None):
        try:
            user = User.objects.get(email=request.data["email"])

            if check_password(request.data["password"], user.password):
                payload = jwt_payload_handler(user)

                token = jwt_encode_handler(payload)

                user.save()
                roles = [{"id": role.id, "name": role.name}
                         for role in user.roles.all()]
                fullname = f"{user.first_name} {user.last_name}"
                
                res = {
                    "msg": "Login success",
                    "success": True,
                    "data": {
                        "name": fullname,
                        "username": user.username,
                        "id": user.id,
                        "token": token,
                        "roles": roles
                    }
                }
                
                return Response(data=res, status=status.HTTP_200_OK)

            else:
                res = {
                    "msg": "Invalid login credentials",
                    "data": None,
                    "success": False
                }
                return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            res = {
                "msg": str(e), 
                "success": False, 
                "data": None
            }
            return Response(data=res, status=status.HTTP_200_OK)