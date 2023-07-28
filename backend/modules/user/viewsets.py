from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from modules.abstract.viewsets import AbstractViewSet
from modules.user.serializers import UserSerializer
from modules.user.models import User
from modules.auth.permissions import UserPermission



class UserViewSet(AbstractViewSet):
    http_method_names = ("patch", "get")
    permission_classes = (
        IsAuthenticated,
        UserPermission,
    )
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True, is_staff=True)

    def get_object(self):
        try:
            instance = User.object.get(id=self.kwargs["pk"])
            self.check_object_permissions(self.request, instance)
            
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404