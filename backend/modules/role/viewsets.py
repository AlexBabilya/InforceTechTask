from abstract.viewsets import AbstractViewSet

from .models import Role
from .serializers import RoleSerializer

class RoleListAPIView(AbstractViewSet):
    http_method_names = ('get')
    serializer_class = RoleSerializer
    
    def get_queryset(self):
        return Role.objects.all()
