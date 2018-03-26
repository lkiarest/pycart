from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class User(AbstractUser):
    openid = models.CharField(max_length=100,blank=True,null=True,verbose_name="openid",unique=True)
    objects = UserManager()