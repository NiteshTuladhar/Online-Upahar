from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
