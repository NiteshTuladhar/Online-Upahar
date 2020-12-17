from django.contrib import admin

from .models import *

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('id','customer', 'date_ordered', 'complete', 'transaction_id')
    search_fields = ('date_ordered', 'transaction_id', 'id')
    readonly_fields = ('customer', 'date_ordered', 'complete', 'transaction_id', 'order_items')
    filter_horizontal = ()
    last_filter = ()
    field_sets = ()


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ('product','quantity','order_id')
    search_fields = ('quantity','product__product_name','order__id')
    readonly_fields = ('product', 'order_id', 'quantity')
    filter_horizontal = ()
    last_filter = ()
    field_sets = ()


class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = ('order','address', 'first_name', 'last_name', 'email','customer') 
    search_fields = ('email','order__id','customer__first_name')
    readonly_fields = ('order','address', 'email','customer')
    filter_horizontal = ()
    last_filter = ()
    field_sets = ()


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Wishlist)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAdress, ShippingAdressAdmin)
