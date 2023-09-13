from django.db import models

# Create your models here.


class Registrationdb(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Profile_Image = models.ImageField(upload_to="registrationimages", null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class Contactdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Query_Topic = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Message = models.TextField(max_length=100, null=True, blank=True)

class MedicineCartdb(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Medicine_Name = models.CharField(max_length=100, null=True, blank=True)
    Manufacturer = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)

class CheckOutdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.CharField(max_length=100, null=True, blank=True)
    Cname = models.CharField(max_length=100, null=True, blank=True)
    Cnum = models.IntegerField(null=True, blank=True)
    Expm = models.CharField(max_length=100, null=True, blank=True)
    Expyear = models.IntegerField(null=True, blank=True)
    Cvv = models.IntegerField(null=True, blank=True)

class Appointmentdb(models.Model):
    Department_Name = models.CharField(max_length=100, null=True, blank=True)
    Doctor_Name = models.CharField(max_length=100, null=True, blank=True)
    Date = models.CharField(max_length=100, null=True, blank=True)
    Time = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Message = models.CharField(max_length=300, null=True, blank=True)


