from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

from modules.auth.handlers import jwt_decode_handler
from .serializers import CreateRestaurantSerializer, RestaurantListSerializer
from .models import Restaurant


class RestaurantCreateAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        req = request.data
        user = {
            'created_by': jwt_decode_handler(request.auth).get('username')
        }
        
        req = dict(request.data)
        req.update(user)
        serializer = CreateRestaurantSerializer(data=req)
        
        if serializer.is_valid():
            serializer.save()
            res = {
                "msg": "Restaurant Created",
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
    
    
class RestaurantListAPIView(ListAPIView):
    serializer_class = RestaurantListSerializer
    queryset = Restaurant.objects.all()