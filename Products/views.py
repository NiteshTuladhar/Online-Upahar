from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Profile.models import Profile
from .models import Product,Wishlist

# Create your views here.


def productDetails(request,slug):

	details = Product.objects.get(slug=slug)
	
	context = {

		'details' : details
	}

	return render(request,'product_details/product_details.html',context)

def wishlist(request, id):
	wishlist = Wishlist.objects.filter(user_id=id)
	id=request.user.id
	print(wishlist)

	context ={
		'wishlist' : wishlist,
		'id': id,

	}

	return render(request, 'product_details/wishlist.html', context)


def wishlist_edit(request, id):
	user = request.user
	product = Product.objects.get(id=id)
	seller_account=product.seller_account
	wish_obj = Product.objects.get(id=product.id)
		
	if request.method == 'GET':
		x = request.GET.get('wish_id')
		print(x)
		if user in wish_obj.liked.all():
			wish_obj.liked.remove(user)
		else:
			wish_obj.liked.add(user)
			
		wish, created = Wishlist.objects.get_or_create(user=user, product_id=wish_obj.id, seller_account=seller_account)

		if not created:
			if wish.liked == 'Wish':
				wish.liked = 'Unwish'
				wish.delete()
				print('---------------remove---------------------')
			else:
				wish.liked = 'Wish'	
				print('================added======================')

			wish.save()  

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_delete(request, id):
	user = request.user.id
	wishlist = Wishlist.objects.get(id=id)
	wishlist.delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
