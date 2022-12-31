from django.db import models
from django.contrib.auth.models import AbstractUser
# from transaction.models import Mas_borrow,Mas_lend

# Create your models here.

class Budget(models.Model):
    income  = models.FloatField()
    lend = models.IntegerField(default= 0)
    borrow = models.IntegerField(default = 0)

class User(AbstractUser):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100,unique = True)
    password = models.CharField(max_length = 100)
    income = models.IntegerField(null=True,blank=True)
    net_income = models.IntegerField(null=True,blank=True)
    job_type = models.CharField(max_length = 100,null=True,blank=True)
    budget = models.ForeignKey(Budget,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


