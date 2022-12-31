from django.db import models
from authentication.models import User

# Create your models here.

class Mas_trans(models.Model):
    made_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="made_by")
    made_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="made_to",null=True,blank=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    # type = models.CharField(max_length=100,null=True,blank=True)# solo or group
    created_at = models.DateTimeField(auto_now_add=True)

