from rest_framework import serializers

from modules.user.models import User
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )
    
    id = serializers.CharField(read_only=True)
    employee_no = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'password',
            'username',
            'id',
            'employee_no',
            'first_name',
            'last_name',
            'email',
            'phone',
            "identification_no",
            "employee_no",
            "roles"
        ]
        
    def create(self, validated_data):
        return User.objects.create_stuff(**validated_data)
        