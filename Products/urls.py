from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Products'

urlpatterns = [
   path('product-details/<slug:slug>', views.productDetails, name='productdetails'),
   path('wishlist/<int:id>', views.wishlist, name='wishlist'),
   path('add-wishlist/<int:id>/', views.wishlist_edit, name='edit_wishlist'),
   path('delete-wishlist/<int:id>', views.wishlist_delete, name='delete_wishlist'),
   path('add-to-cart/<slug:slug>', views.details_add_to_cart, name='add_to_cart'),
   path('delete-add-to-cart/<slug:slug>', views.delete_add_to_cart, name='delete_add_to_cart'),
]