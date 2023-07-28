from django.contrib.auth.models import Group
from rest_framework import serializers

from modules.role.serializers import RoleSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    roles = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "identification_no",
            "roles",
        ]
