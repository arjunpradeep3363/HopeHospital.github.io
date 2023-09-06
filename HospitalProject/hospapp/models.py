from django.db import models

# Create your models here.


class DoctorDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Department_Name = models.CharField(max_length=100,null=True,blank=True)
    Contact_Email = models.CharField(max_length=100,null=True,blank=True)
    Contact_Phone = models.IntegerField(null=True,blank=True)
    Bio = models.TextField(max_length=1000, null=True, blank=True)
    Profile_Picture = models.ImageField(upload_to="doctors", null=True, blank=True)

class NurseDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Contact_Phone = models.IntegerField(null=True, blank=True)
    Bio = models.TextField(max_length=1000, null=True, blank=True)
    Assigned_Department = models.CharField(max_length=100, null=True, blank=True)
    Profile_Picture = models.ImageField(upload_to="nurses", null=True, blank=True)

class DepartmentDb(models.Model):
    Department_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=1000,null=True,blank=True)
    Department_Image = models.ImageField(upload_to="departments",null=True,blank=True)

class PatientDb(models.Model):
    Patient_Name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Contact_Phone = models.IntegerField(null=True, blank=True)
    Medical_History = models.TextField(max_length=100, null=True, blank=True)
    Admitted_Department = models.CharField(max_length=100, null=True, blank=True)
    Insurance_Information = models.CharField(max_length=100, null=True, blank=True)
    Assigned_Doctor = models.CharField(max_length=100,null=True,blank=True)

class MedicineDb(models.Model):
    Medicine_Name = models.CharField(max_length=100, null=True, blank=True)
    Manufacturer = models.CharField(max_length=100, null=True, blank=True)
    Quantity_Stock = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=1000, null=True, blank=True)
    Medicine_Image = models.ImageField(upload_to="medicines",null=True,blank=True)

class StaffLoginDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Re_Password = models.CharField(max_length=100, null=True, blank=True)





