from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategory')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name='products')
    price_new = models.DecimalField(max_digits=5,decimal_places=2)
    desc = models.CharField(max_length=200)
    price_old = models.DecimalField(max_digits=5,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products/")

class Worker(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="worker")
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    age = models.DateField()
    image = models.ImageField(upload_to='workers/')
    role = models.PositiveSmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

class UserPassword(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='passwords')
    password = models.CharField(max_length=100)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)







# Create your models here.
