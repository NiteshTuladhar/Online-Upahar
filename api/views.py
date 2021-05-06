from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from Products.models import *
from Profile.models import Profile
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from Account.token import generatetoken
from Account.models import Account


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


#--------Products Action API---------------------------------------------------------#

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