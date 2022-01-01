from django.db import models


class Product(models.Model):
    name = models.CharField(max_length= 50)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.TextField(blank=True)
    store = models.CharField(max_length=30)
    image = models.CharField(max_length=5000, null = True, blank = True)
