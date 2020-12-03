from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from SellerAccount.models import SellerAccount
from Account.models import Account
from Profile.models import Profile


from django import template

from datetime import datetime, timezone

# Create your models here.

class Product(models.Model):
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True, related_name='seller_account')
    product_name = models.CharField(max_length=50)
    product_details = models.TextField()
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(null=True, upload_to ='product_details_img/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from='product_name',unique=True,null=True,blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    liked = models.ManyToManyField(Account, default=None, blank=True, related_name='liked')

    visit = models.PositiveIntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.product_name


    register = template.Library()


    @register.filter
    def formatted_visit_number(value, num_decimals=2):
    
        int_value = int(visit)
        formatted_number = '{{:.{}f}}'.format(num_decimals)
        if int_value < 1000:
            return str(int_value)
        elif int_value < 1000000:
            return formatted_number.format(int_value/1000.0).rstrip('0.') + 'K'
        else:
            return formatted_number.format(int_value/1000000.0).rstrip('0.') + 'M'


    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url

    def get_add_to_cart_url(self):
        return reverse ("Product:add_to_cart", kwargs={
            'slug' : self.slug
            })

class Category(models.Model):
    product_category = models.CharField(max_length=50)

    def __str__(self):
        return self.product_category



class Order(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200,null=True, unique=True)
    order_items = models.ManyToManyField('OrderItem',related_name='orderitem')

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True

        return shipping
    


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
        
    @property
    def get_cart_grandtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])

        for i in orderitems:
            if i.product.digital == True:
                total = total

            else:
                total = total + 50

        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.product_price*self.quantity
        return total
    
    def __str__(self):
        return self.product.product_name


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True,
    )
    date_added = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'wishlisted by {self.user.account_name}'


