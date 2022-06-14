from distutils.command.upload import upload
from django.db import models
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=30)
    pid = models.CharField(max_length=12)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    img = models.ImageField(upload_to = 'images')
    def __str__(self):
        return self.title

class Signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class productdetails(models.Model):
    productName = models.CharField(max_length=50)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to = 'product_images/',blank='true',null='true')
    userid = models.ForeignKey(Signup,on_delete=models.CASCADE)
    
class Apiusers(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



