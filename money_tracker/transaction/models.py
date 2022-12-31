from django.db import models
from authentication.models import User

# Create your models here.

class Mas_trans(models.Model):
    made_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="made_by")
    made_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="made_to",null=True,blank=True)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    type = models.CharField(max_length=100,null=True,blank=True)# solo or group
    created_at = models.DateTimeField(auto_now_add=True)



class Groups_trans(models.Model):
    group_name = models.CharField(max_length=100,unique=True)
    grp_made_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="grp_made_by",null=True,blank=True)
    grp_trans_made_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="grp_trans_made_to",null=True,blank=True)
    # grp_trans_id = models.OneToOneField(Mas_trans,on_delete=models.CASCADE)
    desc = models.CharField(max_length=500)
    grp_members = models.ManyToManyField(User,related_name= "grp_member")
    no_of_per = models.IntegerField(default  = 0)
    amount_pp = models.FloatField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)



    

# class Mas_lend(models.Model):
#     lend_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name="lend_to")
#     amount = models.FloatField()
#     updated_at = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)


# class Mas_borrow(models.Model):
#     borrow_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name="borrow_from")
#     amount = models.FloatField()
#     updated_at = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)


