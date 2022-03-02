from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)    
    name = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    weight = models.IntegerField(blank = True, null = True)
    description = models.TextField(blank=True)
    store = models.CharField(max_length=30)
    image = models.CharField(max_length=5000, null = True, blank = True)

    def __str__(self):
        return self.name

    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null = True, blank = True)
