from rest_framework import serializers

from .models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class CreateRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "name",
            "contact_no",
            "address",
        ]
        model = Restaurant
