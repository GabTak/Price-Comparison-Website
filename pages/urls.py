from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name = 'home'),
    path('help/', views.help_page_view , name = 'help'),
    path('basket/', views.basket_page_view, name = 'basket'),
    path('contents/', views.contents_page_view, name = 'contents')

]