from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request, *args, **kwargs):
    return render(request, "home.html")

def help_page_view(request, *args, **kwargs):
    return render(request, "help.html")

def basket_page_view(request, *args, **kwargs):
    return render(request, "basket.html")

def contents_page_view(request,*args, **kwargs):
    return render(request, "contents.html")