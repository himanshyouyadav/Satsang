from email.policy import default
from inspect import signature
from pyexpat import model
from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User

# Create your models here.


# class MemberDetails:

class Member(models.Model):
    #Personal
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    Age = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()
    # Permanent Add
    perma_street = models.CharField(max_length=200,null=True)
    perma_city = models.CharField(max_length=200,null=True)
    perma_state = models.CharField(max_length=200)
    perma_pin = models.IntegerField()
    # Present Add
    pres_street = models.CharField(max_length=200,null=True)
    pres_city = models.CharField(max_length=200,null=True)
    pres_state = models.CharField(max_length=200)
    pres_pin = models.IntegerField()

    # Profession and Education
    education = models.CharField(max_length=200,null=True)
    profession = models.CharField(max_length=200,null=True)

    #Religion
    religion = models.CharField(max_length=200,null=True)
    varna = models.CharField(max_length=200,null=True)

    # Confirmation
    signature = models.ImageField(null=True,blank=True,upload_to = "images/account/member/signature")

    ritwik = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
   
    def __str__(self):
        return self.first_name 


