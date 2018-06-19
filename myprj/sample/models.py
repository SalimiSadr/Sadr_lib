from django.db import models

# Create your models here.
class developer(models.Model):
    name = models.CharField(max_length=255, )
    family_name = models.CharField(max_length=255, )

    def __str__(self):
        return f"{self.name} {self.family_name}"