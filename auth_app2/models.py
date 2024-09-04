from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AuthUserModel(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null = True)
    address = models.CharField(max_length=100, null = True)
    phone_number = models.CharField(max_length=10, null = True)
    
    