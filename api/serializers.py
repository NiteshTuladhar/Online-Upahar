from rest_framework import serializers
from Products.models import *
from Cms.models import *


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

#--------------END OF PRODUCTS ACTION SERIALIZERS----------------------#


#--------------ORDER SERIALIZERS----------------------#

class OrderSerializer(serializers.ModelSerializer):

    customer_name = serializers.ReadOnlyField(source='customer')
    order_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Order
        fields = ['order_id','customer_name','date_ordered','complete','transaction_id','order_items']


class OrderItemsSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField(source="product.id", read_only=True)
    product_name = serializers.CharField(source="product.product_name", read_only=True)
    product_description = serializers.CharField(source="product.product_details", read_only=True)
    product_price = serializers.IntegerField(source="product.product_price", read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_id','product_name','product_description','product_price','order','quantity','date_added']


#--------------END OF ORDER  SERIALIZERS----------------------#




#--------------USER PROFILE SERIALIZERS----------------------#
class ProfileSerializer(serializers.ModelSerializer):


    
    profile_id = serializers.ReadOnlyField(source='id')
    profile_user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['profile_id','profile_user','first_name','last_name','phone','mobile','profile_image','gender','location']
    


#--------------ABOUT US SERIALIZERS----------------------#

class AboutUsSerializer(serializers.ModelSerializer):


    
    aboutus_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = AboutUs
        fields = ['aboutus_id','title','body']

class TermsAndConditionSerializer(serializers.ModelSerializer):


    
    termandcondition_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = TermsAndConditions
        fields = ['termandcondition_id','title','body']


class PrivacyAndPolicySerializer(serializers.ModelSerializer):

    privacyAndPolicy_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = PrivacyAndPolicy
        fields = ['privacyAndPolicy_id','title','body']