from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    def __str__(self):
        return self.name