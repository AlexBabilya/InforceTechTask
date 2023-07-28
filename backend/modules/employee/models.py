from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    """Represents employee class model"""

    employee_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
