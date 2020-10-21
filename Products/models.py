from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from SellerAccount.models import SellerAccount
from Account.models import Account
from Profile.models import Profile
# Create your models here.

class Product(models.Model):
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50)
    product_details = models.TextField()
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(null=True, upload_to ='product_details_img/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from='product_name',unique=True,null=True,blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ''
        return url

class Category(models.Model):
    product_category = models.CharField(max_length=50)

    def __str__(self):
        return self.product_category



class Order(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200,null=True)

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
            if i.product.digital == False:
                grandtotal = total + 50
            else:
                grandtotal = total
        return grandtotal

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
    
class ShippingAdress(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    zone = models.CharField(max_length=200,null=True)
    postal_code = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'wishlisted by {self.user.account_name}'


