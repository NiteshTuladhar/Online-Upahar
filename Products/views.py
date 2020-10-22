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
	print(product)
	wishlist = Wishlist(user=user, seller_account=seller_account, product=product)
	wishlist.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_delete(request, id):
	user = request.user.id
	wishlist = Wishlist.objects.get(id=id)
	wishlist.delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
