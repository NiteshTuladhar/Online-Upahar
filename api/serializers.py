from rest_framework import serializers
from Products.models import *


#--------------PRODUCTS SERIALIZERS----------------------#
class ProductSerializer(serializers.ModelSerializer):

    product_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Product
        fields = ['product_id','seller_account','product_name','product_details','product_image','product_price','category',
                    'subcategory','slug','digital','liked','visit','date']


class ProductImageSerializer(serializers.ModelSerializer):

    product_image_id = serializers.ReadOnlyField(source='id')
    product_id = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = ProductImage
        include = ['product_image_id','product_id']
        exclude = ['id','product']


class CategoriesSerializer(serializers.ModelSerializer):
    
    category_id = serializers.ReadOnlyField(source='id')
    

    class Meta:
        model = Category
        include = ['category_id']
        exclude = ['id']



class MainCategoriesSerializer(serializers.ModelSerializer):

    main_category_id = serializers.ReadOnlyField(source='id')
    main_category_slug = serializers.ReadOnlyField(source='slug')

    class Meta:
        model = MainCategory
        include = ['main_category_id','main_category_slug']
        exclude = ['id','slug']



class SubCategoriesSerializer(serializers.ModelSerializer):

    sub_category_id = serializers.ReadOnlyField(source='id')
    main_category_id = serializers.ReadOnlyField(source='category.id')
    sub_category_slug = serializers.ReadOnlyField(source='slug')

    class Meta:
        model = SubCategory
        include = ['sub_category_id','sub_category_slug','main_category_id']
        exclude = ['id','slug','category']

#--------------END OF PRODUCTS SERIALIZERS----------------------#




#--------------PRODUCTS ACTIONS SERIALIZERS----------------------#

class WishlistSerializer(serializers.ModelSerializer):

    wishlist_id = serializers.ReadOnlyField(source='id')
    user = serializers.ReadOnlyField(source='user.id')
    product = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = Wishlist
        fields = ['wishlist_id','user','product']