from os import name
from django.db import models

# Create your models here.

class PrimaryAddress(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField("Address line 1",max_length=100)
    address2 = models.CharField("Address line 2",max_length=100)
    pin_code = models.CharField("Postal code",max_length=12)
    village = models.CharField("Village",max_length=50)
    city = models.CharField("City",max_length=50)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12,unique=True)
    primary_address = models.ForeignKey(PrimaryAddress, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField("Address line 1",max_length=100)
    address2 = models.CharField("Address line 2",max_length=100)
    pin_code = models.CharField("Postal code",max_length=12)
    village = models.CharField("Village",max_length=50)
    city = models.CharField("City",max_length=50)
    country = models.CharField(max_length=100)
    farmer = models.ForeignKey(Farmer ,on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name
    