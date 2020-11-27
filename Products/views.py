from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Profile.models import Profile
from .models import Product,Wishlist
from Products.models import Product,Order, OrderItem, ShippingAdress
import time
# Create your views here.


def productDetails(request,slug):

	product_visit = Product.objects.get(slug=slug)


	product_visit.visit = product_visit.visit + 1
	product_visit.save()

	if request.user.is_authenticated:
		details = Product.objects.get(slug=slug)
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		details = Product.objects.get(slug=slug)
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context={'details' : details,'items' : items, 'order':order,'cartItems':cartItems}
	
	
	return render(request,'product_details/product_details.html',context)



def wishlist(request, id):

	
	wishlist = Wishlist.objects.filter(user_id=id)
	id=request.user.id
	print(wishlist)

	if request.user.is_authenticated:
		customer = request.user.profile
		print(customer)
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print(items)
	else:
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context={'items' : items, 'order':order,'cartItems':cartItems,'wishlist' : wishlist,'id': id,}



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
			wish = Wishlist.objects.get(user=user, product_id=product.id, seller_account=seller_account)
			wish.delete()
		else:
			wish_obj.liked.add(user)
			wish, created = Wishlist.objects.get_or_create(user=user, product_id=wish_obj.id, seller_account=seller_account)
			wish.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def wishlist_delete(request, id):
	user = request.user.id
	wishlist = Wishlist.objects.get(id=id)
	product = wishlist.product.id
	wish_obj = Product.objects.get(id=product)
	wishlist.delete()
	wish_obj.liked.remove(user)


	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def details_add_to_cart(request,slug):
 
	item = get_object_or_404(Product, slug=slug)
	order, created = Order.objects.get_or_create(

		customer=request.user.profile,
		complete=False

    )
	print(order.order_items)
	print('===============================================')
	if order.order_items.filter(product__slug=item.slug).exists():

		itemorder.quantity +=1
		itemorder.save()

		print('iffffffffffffffff')
	else:
		print('elseeeeeeeeeeeee')
		itemorder, created = OrderItem.objects.get_or_create(
	        product=item,
	        order = order,
	        quantity= 1,

	    )
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))