from rest_framework import serializers

from modules.user.serializers import UserSerializer
from modules.user.models import User


class UserRegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation
    """

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "roles",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
