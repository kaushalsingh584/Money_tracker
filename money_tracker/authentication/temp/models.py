from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100,unique = True)
    password = models.CharField(max_length = 100)
    income = models.IntegerField(null=True,blank=True)
    net_income = models.IntegerField(null=True,blank=True)
    job_type = models.CharField(max_length = 100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']