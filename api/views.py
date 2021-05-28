from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from Products.models import *
from Profile.models import *
from Store.models import *
from Cms.models import *
from Profile.models import *
from Cms.models import *
from Reviews.models import *
from django.views.decorators.csrf import csrf_exempt
from ContactMail.mail import CustomMail
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from Account.token import generatetoken
from Account.models import Account
from django.urls import reverse
import json
import datetime
import requests
#-----------------------Account Models API-----------------------------------#

@api_view(['POST'])
def signup(request):

    data = request.data
    
    try:
        account = Account(email=data['email'], account_name=data['account_name'])
        account.set_password(data['password'])
        account.token = generatetoken()
        account.save()

        return JsonResponse({'token': account.token },status=201)
    except:

        return JsonResponse({'error':'The username or email has already been taken'},status=400)

    return JsonResponse({'error' : "some error occured"},status=400)
    


@api_view(['POST'])
def login(request):

    data = request.data
    user = authenticate(request, email=data['email'], password=data['password'])

    if user is None:
        return JsonResponse({'error':'No user found'})
    else:
  
        token = Account.objects.get(id=user.id).token
        return JsonResponse({'token':str(token)})



@api_view(['GET'])
def verify_account(request,id,token,backend='django.contrib.auth.backends.ModelBackend'):

    data = request.data

    a = Account.objects.get(id=id)

    if a.is_verified == False:

        if a.token == token:
            a.is_verified = True
            profile = Profile(user=a)
            profile.save()
            a.save()
            if a.profile_create is False:
                a.profile_create = True
                a.save()

            return JsonResponse({'success':'Your account has been verified'},status=200)

        else:
            return JsonResponse({'error':'Some error occured'},status=400)

    else:
        return JsonResponse({'error':'Your account is already activated. Hey!! It\'s a great time to create your profile'})

    return JsonResponse({'error':'Some error occured'})


#-----------------------End of Account Models API-----------------------------------#




#-----------------------Product Models API-----------------------------------#

class AllProductsList(generics.ListAPIView):

    serializer_class = ProductSerializer


    def get_queryset(self):

        return Product.objects.all()


class AllProductImageList(generics.ListAPIView):

    serializer_class = ProductImageSerializer


    def get_queryset(self):

        return ProductImage.objects.all()



@api_view(['GET'])
def getProductDetails(request, id):

    query_set = Product.objects.get(id=id)
    serializers = ProductSerializer(query_set, many=False) 

    return Response(serializers.data)

     
class CategoriesList(generics.ListAPIView):

    serializer_class = CategoriesSerializer


    def get_queryset(self):

        return Category.objects.all()


class MainCategoriesList(generics.ListAPIView):

    serializer_class = MainCategoriesSerializer


    def get_queryset(self):

        return MainCategory.objects.all()


class SubCategoriesList(generics.ListAPIView):

    serializer_class = SubCategoriesSerializer


    def get_queryset(self):

        return SubCategory.objects.all()

#-----------------------End of Products Models API-----------------------------------#


#--------Products Wishlist API---------------------------------------------------------#

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWishlist(request):

    query_set = Wishlist.objects.filter(user_id=request.user.id)
    serializers = WishlistSerializer(query_set,many=True)

    return Response(serializers.data)



@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def addRemoveWishlist(request,id):

    product = Product.objects.get(id=id)
    user = request.user
    seller_account=product.seller_account

    if user in product.liked.all():
        product.liked.remove(user)
        wish = Wishlist.objects.get(user=user, product_id=product.id, seller_account=seller_account)
        wish.delete()
        return Response({'success':'Product removed from the wishlist'})
    else:
        product.liked.add(user)
        wish, created = Wishlist.objects.get_or_create(user=user, product_id=product.id, seller_account=seller_account)
        wish.save()
        return Response({'success':'Product added to the wishlist'})
        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deleteWishlistItem(request,id):

    user = request.user.id
    
    try:
        wishlist_product = Wishlist.objects.get(id=id,user_id=user)
        product_id = wishlist_product.product.id
        product = Product.objects.get(id=product_id)
        wishlist_product.delete()
        product.liked.remove(user)
        return Response({'success':'Product has been removed from your wishlist.'})
    except:
        return Response({'error':'Product not found.'})




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addWishlistToCart(request,id):

    user = request.user.id
    wishlist = Wishlist.objects.get(id=id)
    product = wishlist.product.id
    item = Product.objects.get(id=product)

    order, created = Order.objects.get_or_create(

        customer=request.user.profile,
        complete=False

    )

    if OrderItem.objects.filter(product=item, order = order).exists():
        x = OrderItem.objects.get(product=item, order = order)
        print(x)
        x.quantity +=1
        x.save()
        wishlist.delete()
        return Response({'success':'The product quantity has been increased.'})

    else:
        itemorder, created = OrderItem.objects.get_or_create(
            product=item,
            order = order,
            quantity= 1,
            
        )

        wishlist.delete()

        return Response({'success':'Your wishlist item has been added to cart'})


#-----------------------------End of Wishlist API----------------------------------#



#-----------------------------Details Add to Cart API----------------------------------#

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addToCartDetailsPage(request,slug):

    item = Product.objects.get(slug=slug)
    order, created = Order.objects.get_or_create(

        customer=request.user.profile,
        complete=False

    )
    if OrderItem.objects.filter(product=item, order = order).exists():
        x = OrderItem.objects.get(product=item, order = order)
        print(x)
        x.quantity +=1
        x.save()
        return Response({'success':'The product quantity has been increased.'})
    else:
        itemorder, created = OrderItem.objects.get_or_create(
            product=item,
            order = order,
            quantity= 1,
        )
        return Response({'success':'The product has been added to the cart.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteAddToCart(request,slug):

    order = Order.objects.get(customer=request.user.profile, complete=False)
    item = Product.objects.get(slug=slug)
    items = OrderItem.objects.get(order= order, product=item)
    items.delete()

    return Response({'success':'Your cart items has been deleted.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buyNow(request,slug):

    category = Category.objects.all()
    item = Product.objects.get(slug=slug)
    order, created = Order.objects.get_or_create(

        customer=request.user.profile,
        complete=False

    )
    
    if OrderItem.objects.filter(product=item, order = order).exists():
        x = OrderItem.objects.get(product=item, order = order)
        print(x)
        
    else:
        itemorder, created = OrderItem.objects.get_or_create(
            product=item,
            order = order,
            quantity= 1,

        )

    if request.user.is_authenticated:
        customer = request.user.profile
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        print(items)
    else:
        customer = 'Anonymous User'
        items = []
        order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    return Response({'success':'your product is ready for checkout'})


#-----------------------------End of Details Add To Cart API----------------------------------#



#-----------------------------Contact Mail Sending API----------------------------------#

@api_view(['POST'])
def mailsendContact(request):

    try:
        data = request.data
        hostemail = 'sushek69@gmail.com'
        name = data['name']
        email = data['email']
        subjects = data['subject']
        number = data['phone']
        textmessage = data['message']
        mail = CustomMail('mail/email_template.html', 'From Website Mail Notification', [hostemail,], nameofcustomer=name, numberofcustomer=number, messageofcustomer=textmessage, emailofcustomer=email, subjects=subjects)
        mail.push()
        
        return Response({'success': 'Your Message Has Been Received'})

    except:
        return Response({'error': 'Some Error Occured.'})

#-----------------------------End of Contact Mail Sending API------------------#


#----------------------------Store API-----------------------------------------#



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def usersOrder(request):

    customer_profile = Profile.objects.get(user=request.user)
    profile_serializer = ProfileSerializer(customer_profile,many=False)

    profile_datas = profile_serializer.data

    query_set = Order.objects.get(customer=customer_profile,complete=False)

    serializers = OrderSerializer(query_set,many=False)
    
    datas = serializers.data


    o_id = datas['order_id']
    f_name = profile_datas['first_name']
    l_name = profile_datas['last_name']
  
    date_ord  = datas['date_ordered']
    complete = datas['complete']
    transaction_id = datas['transaction_id']
    order_items = datas['order_items']

    return Response(
        {
            'order_id' : o_id,
            'customer_name' : f_name,
            'last_name' : l_name,
            'date_ordered' :date_ord,
            'complete': complete,
            'transaction_id': transaction_id,
            'order_items': order_items,
        
        }
    )


#----------------------------End of Store API----------------------------------#


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cartPage(request):

    customer_profile = Profile.objects.get(user=request.user)

    order = Order.objects.get(customer=customer_profile,complete=False)
    
    query_set = OrderItem.objects.filter(order=order)

    serializers = OrderItemsSerializer(query_set,many=True)
    

    return Response(
          
            serializers.data
    )


#----------------------------End of Store API----------------------------------#


#---------------------------START of Profile API ---------------------------------


@permission_classes([IsAuthenticated])
class ProfilePage(generics.ListAPIView):
    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ownProfilePage(request):

    query_set = Profile.objects.get(user_id=request.user.id)
    
    
    serializers = ProfileSerializer(query_set,many=False)

    return Response(serializers.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orderHistory(request):

    profile = Profile.objects.get(user_id=request.user.id)
    query_set = Order.objects.filter(customer=profile, complete=True)



    all_orders = []

    for order in query_set:

        myorder_items = OrderItem.objects.filter(order_id=order.id)

        all_orders.append(myorder_items)



    total_items = []

    for item in all_orders:
        for i in item:
            total_items.append(i)		


    

    serializers = OrderItemsSerializer(total_items,many=True)
    return Response(serializers.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editOwnProfilePage(request):

    data = request.data
    first_name =  data.get('first_name')
    last_name =  data.get('last_name')
    phone =  data.get('phone')
    mobile =  data.get('mobile')
    gender =  data.get('gender')
    location =  data.get('location')


    p = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
	    p.first_name = first_name
	    p.last_name = last_name
	    p.phone = phone
	    p.mobile = mobile
	    p. gender = gender
	    p.location = location

	    try:
	        p.save()
	        return Response({'success':'your profile has been updated'})
	    except:
		    return Response({'error':'Erro occured'})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ownProfileEdit(request):
    data = request.data
    images = data.get('profile_image')
    print(images)
    profile = Profile.objects.get(user__id=request.user.id)
    profile.profile_image = images
    
    try:
	    profile.save()
	    return Response({'success':'your profile has been updated'})
    except:
        return Response({'success':'your profile has been updated'})
#---------------------------END OF PROFILE API -----------------------------------------


#--------------------------Start of CMS API ---------------------------------------------

class AboutUsPage(generics.ListAPIView):
    
    serializer_class = AboutUsSerializer

    def get_queryset(self):
        return AboutUs.objects.all()


class TermsAndConditionPage(generics.ListAPIView):
    
    serializer_class = TermsAndConditionSerializer

    def get_queryset(self):
        return TermsAndConditions.objects.all()


class PrivacyAndPolicyPage(generics.ListAPIView):
    
    serializer_class = TermsAndConditionSerializer

    def get_queryset(self):
        return PrivacyAndPolicy.objects.all()


#---------------------------END OF CMS API -----------------------------------------


#--------------------------REVIEW API----------------------------------------------


@api_view(['GET'])
def productReview(request,slug):
    
    product_visit = Product.objects.get(slug=slug)
    print(product_visit)
    print('-----------------pv')
    query_set = Review.objects.filter(product=product_visit, reply=None).order_by('-comment_time')

    serializers = ReviewSerializer(query_set,many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def giveReview(request, slug):

    user = request.user
    profile = Profile.objects.get(user=user)
    product = Product.objects.get(slug=slug)


    data = request.data

    try:
        review = Review(user=user,profile=profile,product=product,message=data['message'])
        review.save()

        return JsonResponse({'success': 'Your review has been saved' })
    
    except:
        return JsonResponse({'error':'Some error occured'})
    


#-------------------------END OF REVIEW API----------------------------------------
