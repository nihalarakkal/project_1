from django.db import models

# Create your models here.
class category_db(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="category Images",null=True,blank=True)
class product_db(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    Product_Name=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Product_Image = models.ImageField(upload_to="product images", null=True, blank=True)
