from rest_framework import serializers
from Products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['seller_account','product_name','product_details','product_image','product_price','category',
                    'subcategory','slug','digital','liked','visit','date']



        