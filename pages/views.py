from django.shortcuts import render
from product.models import *
from django.db.models import Q
from django.db.models import Max

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

    
    #Search items by name, store and description
    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(Q(name__icontains=q) | Q(store__icontains=q) | Q(description__icontains=q))
        
    else:
        products = Product.objects.all()

    #Price range
    if 'min_price' in request.GET or 'max_price' in request.GET:
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        if min_price == '':
            min_price = 0
        if max_price == '':
            max_price = Product.objects.all().aggregate(Max('price'))
            max_price = max_price.get('price__max')

        products = products.filter(price__range=(min_price, max_price))

    #Stores
    tesco = request.GET.get('Tesco')
    morrisons = request.GET.get('Morrisons')
    waitrose = request.GET.get('Waitrose')
    sainsburys = request.GET.get("Sainsburys")
    stores_to_display = set()

    #Get list of stores to display
    if tesco:
        stores_to_display.add('Tesco')
    if morrisons:
        stores_to_display.add('Morrisons')
    if sainsburys:
        stores_to_display.add('Sainsburys')
    if waitrose:
        stores_to_display.add('Waitrose')
    
    
    if (len(stores_to_display) == 0):
        products
    else:
        products = products.filter(store__in=(stores_to_display))



    
    context ={'products' : products.order_by('price')}
    
    return render(request, "contents.html", context)

