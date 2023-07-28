from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Role
        fields = ["id", "name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]
