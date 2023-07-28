from rest_framework import serializers

from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name']
