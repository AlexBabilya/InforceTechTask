from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    password = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True} }
        read_only_fields = ('id',)
