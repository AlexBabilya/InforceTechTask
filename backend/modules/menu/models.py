from django.db import models

from modules.restaurant.models import Restaurant


class Menu(models.Model):
    """Represents menu class model"""

    restaurant = models.ForeignKey(
        Restaurant, null=True, blank=True, on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="menus/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.CharField(max_length=50, null=True, blank=True)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.restaurant.name
