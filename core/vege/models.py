from django.db import models
from django.contrib.auth.models import User


class Vege(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vegetables/')

    def __str__(self):
        return self.name
