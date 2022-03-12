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
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name

    #Prevent error when no image is present for product
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null= True, blank= True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null = True)
    quantity = models.IntegerField(default=0, null = True, blank = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
