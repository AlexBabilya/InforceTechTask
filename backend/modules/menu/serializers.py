from rest_framework import serializers

from .models import Menu


class MenuUploadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        menu = Menu(
            file=validated_data["file"],
            restaurant=validated_data["restaurant"],
            uploaded_by=validated_data["uploaded_by"],
        )
        menu.save()
        return menu

    class Meta:
        fields = ["restaurant", "file", "uploaded_by"]
        model = Menu


class MenuListSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = "__all__"


class MenuResultListSerializer(serializers.ModelSerializer):
    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "file", "restaurant", "votes", "created_at"]
