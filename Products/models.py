from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from SellerAccount.models import SellerAccount
from Account.models import Account
# Create your models here.

class Product(models.Model):
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50)
    product_details = models.TextField()
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(null=True, upload_to ='product_details_img/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = AutoSlugField(populate_from='product_name',unique=True,null=True,blank=True)

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

class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'wishlisted by {self.user.account_name}'