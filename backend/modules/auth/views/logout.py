from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from modules.user.models import User
from ..handlers import jwt_decode_handler, jwt_encode_handler, jwt_payload_handler


class UserLogoutView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            username = jwt_decode_handler(request.auth).get("username")
            user = User.objects.get(username=username)

            payload = jwt_payload_handler(user)
            jwt_encode_handler(payload)

            res = {"msg": "User logged out successfully", "success": True, "data": None}
            return Response(data=res, status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
