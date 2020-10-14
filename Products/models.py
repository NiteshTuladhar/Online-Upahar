from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_details = models.TextField()
    product_price = models.PositiveIntegerField()
    product_image = models.ImageField(null=True, upload_to ='product_details_img/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

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