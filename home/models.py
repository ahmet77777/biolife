from django.db import models
from django.contrib.auth.models import User
from a_panel.models import *

class Activ(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="activecode")
    pincode = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    status = models.BooleanField(default=False)
    craete_at = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def totalsum(self):
        price = 0
        for i in self.items.all():
            price += i.total_price()
        return price
    
    
    def shipping(self):
        if self.totalsum() > 100:
            return '0'
        else:
            return '50'
        
    def totalsum_full(self):
        price = 0
        for i in self.items.all():
            price += i.total_price()
        price += int(self.shipping())

        return price
 

    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_c')
    quatity = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quatity * self.product.price_new
    
    def total_price_old(self):
        return self.quatity * self.product.price_old

class Order(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='order')
    payment_type = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    status_2 = models.PositiveIntegerField(default=0)
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='wishlist')

class WishlistItems(models.Model):
    wishlist = models.ForeignKey(Wishlist,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wish_product')
    


    

# Create your models here.
