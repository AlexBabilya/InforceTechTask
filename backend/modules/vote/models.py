from django.db import models

from modules.employee.models import Employee
from modules.menu.models import Menu


class Vote(models.Model):
    """Represents vote class model"""

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee}"
