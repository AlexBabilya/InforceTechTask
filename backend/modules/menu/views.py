from django.db.models import Q
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from modules.auth.handlers import jwt_decode_handler
from .models import Menu
from.serializers import MenuUploadSerializer, MenuListSerializer


class MenuUploadAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            req = request.data.dict()
            todays_date = settings.CURRENT_DATE.date()
            menu = Menu.objects.filter(
                Q(restaurant__id=int(req.get('restaurant')))
                and Q(created_at__date=todays_date)
            )
            user = jwt_decode_handler(request.auth).get('username')

            if menu.exists():
                res = {
                    "msg": "Menu already added.",
                    "success": False,
                    "data": None
                }
                return Response(data=res, status=status.HTTP_200_OK)

            serializer = MenuUploadSerializer(data=req)

            if serializer.is_valid():
                serializer.save(uploaded_by=user)
                res = {
                    "msg": "Menu uploaded",
                    "success": True,
                    "data": serializer.data
                }
                return Response(data=res, status=status.HTTP_201_CREATED)

            res = {
                "msg": str(serializer.errors),
                "success": False,
                "data": None
            }
            
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {
                "msg": str(e), 
                "success": False, 
                "data": None
            }
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
        
        
class CurrentDayMenuList(APIView):
    def get(self, request):
        todays_date = settings.CURRENT_DATE.date()

        qs = Menu.objects.filter(Q(created_at__date=todays_date))
        serializer = MenuListSerializer(qs, many=True)
        res = {
            "msg": 'success', 
            "data": serializer.data, 
            "success": True
        }
        return Response(data=res, status=status.HTTP_200_OK)
        
        