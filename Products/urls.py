from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Products'

urlpatterns = [
   path('product-details/<slug:slug>',views.productDetails,name='productdetails'),
]