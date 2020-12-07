"""onlineupahar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Store'

urlpatterns = [
   path('',views.home,name='homepage'),
   path('cart/',views.cartpage,name='cartpage'),
   path('checkout/',views.checkoutpage,name='checkoutpage'),
   path('categories/',views.categoriesItem,name='categoriesItem'),
   path('maincategory/<slug:slug>/',views.maincategoriesItem, name='maincategoriesitem'),
   path('subcategory/<slug:slug>/',views.subcategoriesItem, name='subcategoriesitem'),
   path('update_item/',views.updateItem,name='update_item'),
   path('process_order/',views.processOrder,name='process_order'),
   path('about_us/',views.aboutUs,name='about_us'),
]
