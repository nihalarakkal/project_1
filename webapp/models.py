from django.db import models

# Create your models here.
class contact_db(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
class login_db(models.Model):
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,blank=True,null=True)
class Cart_db(models.Model):
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Total_Price=models.IntegerField(null=True,blank=True)