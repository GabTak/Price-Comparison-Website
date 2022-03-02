from django.shortcuts import render
from product.models import *

# Create your views here.

def home_page_view(request, *args, **kwargs):
    return render(request, "home.html")

def help_page_view(request, *args, **kwargs):
    return render(request, "help.html")

def basket_page_view(request, *args, **kwargs):
    order, created = Order.objects.get_or_create(complete = False)
    items = order.orderitem_set.all()
    context = {'items' : items}

    return render(request, "basket.html", context)

def contents_page_view(request,*args, **kwargs):
    products = Product.objects.all()
    context = {'products' : products}
    
    return render(request, "contents.html", context)

