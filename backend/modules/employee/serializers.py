from rest_framework import serializers

from modules.user.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    employee_no = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "id",
            "employee_no",
            "first_name",
            "last_name",
            "email",
            "phone",
            "identification_no",
            "employee_no",
        ]
