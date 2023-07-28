from django.db import models


class Role(models.Model):
    """
    Represents role class model
    """
    
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}"