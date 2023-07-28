import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from modules.role.models import Role
from .managers import CustomUserManager


class User(AbstractUser):
    """Represents user class model"""

    id = models.CharField(
        max_length=100, unique=True, default=uuid.uuid4, primary_key=True
    )

    roles = models.ManyToManyField(Role, blank=True)
    org_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    identification_no = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    # objects = CustomUserManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
