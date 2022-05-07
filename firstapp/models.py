from email.policy import default
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from .models import *
from pickle import TRUE
from tkinter import Widget
from datetime import datetime, time
# Create your models here.
#class Photo:
 #   id:int
  #  name:str
   # address:str
    #img:str
    #number:int


#role_choice = (
 #   ("1", "Customer"),
  #  ("2", "Administrator"),
   # ("3", "Vendor")

#)
class Dealer(models.Model):

    dealer = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    #image = models.ImageField(upload_to='images/')
    role=models.CharField(max_length=20)


class Vehicle(models.Model):
    vehicle_no=models.CharField(default=None,max_length=20,unique=True)
    vehicle_name=models.CharField(default=None,max_length=20)
    color=models.CharField(max_length=10)
    owner=models.ForeignKey(Dealer,default=None,on_delete=models.CASCADE)
    vehicle_photo=models.ImageField(default=None,upload_to='images/')
    owner_photo=models.ImageField(default=None,upload_to='images/')
    driving_license=models.ImageField(default=None,upload_to='images/')
    citizenship_front=models.ImageField(default=None,upload_to='images/')
    citizenship_back=models.ImageField(default=None,upload_to='images/')
    is_booked=models.BooleanField(default=False)

class Booking(models.Model):
    starttime=models.DateField(default=None)
    endtime=models.DateField(default=None)
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,default=None,on_delete=models.CASCADE)
    is_booked=models.BooleanField(default=False)

class data_model(models.Model):
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    count = models.CharField(max_length=50, null=True)