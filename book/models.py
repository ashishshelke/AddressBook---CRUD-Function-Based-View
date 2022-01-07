from os import name
from django.db import models

# Create your models here.

class Data(models.Model):
    name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=70)