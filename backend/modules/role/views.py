from rest_framework import generics

from .models import Role
from .serializers import RoleSerializer


class RoleListAPIView(generics.ListAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()