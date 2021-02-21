from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Profile.models import Profile
from Reviews.models import Review
from .models import Product,Wishlist
from Products.models import Product,Order, OrderItem, ShippingAdress
import time
from django.utils import timezone
# Create your views here.


def productDetails(request,slug):
	if request.method == 'GET':
		product_visit = Product.objects.get(slug=slug)

		review = Review.objects.filter(product=product_visit, reply=None).order_by('-comment_time')
		product_visit.visit = product_visit.visit + 1
		product_visit.save()

		if request.user.is_authenticated:
			details = Product.objects.get(slug=slug)
			customer = request.user.profile
			order, created = Order.objects.get_or_create(customer=customer,complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else:
			customer = 'Anonymous User'
			details = Product.objects.get(slug=slug)
			items = []
			order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
			cartItems = order['get_cart_items']


		context={'details' : details,'items' : items, 'order':order,'cartItems':cartItems, 'review':review,'customer':customer}
		
		
		return render(request,'product_details/product_details.html',context)

	else:
		product_visit = Product.objects.get(slug=slug)
		profile = Profile.objects.get(user_id=request.user.id)
		message = request.POST.get('message')
		time = timezone.now()
		review_qs = None
		review = Review.objects.create(message=message, product=product_visit,user=request.user,reply=review_qs,profile=profile, comment_time=time)
		return HttpResponseRedirect(request.path_info)


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
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context={'items' : items, 'order':order,'cartItems':cartItems,'wishlist' : wishlist,'id': id,'customer':customer}



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



def wishlist_add_to_cart(request, id):
	user = request.user.id
	wishlist = Wishlist.objects.get(id=id)
	product = wishlist.product.id
	item = Product.objects.get(id=product)

	order, created = Order.objects.get_or_create(

		customer=request.user.profile,
		complete=False

    )
	print(order.order_items)

	if OrderItem.objects.filter(product=item, order = order).exists():
		x = OrderItem.objects.get(product=item, order = order)
		print(x)
		x.quantity +=1
		x.save()

	else:
		itemorder, created = OrderItem.objects.get_or_create(
	        product=item,
	        order = order,
	        quantity= 1,

	    )


	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def details_add_to_cart(request,slug):
 
	item = Product.objects.get(slug=slug)
	order, created = Order.objects.get_or_create(

		customer=request.user.profile,
		complete=False

    )
	print(order.order_items)
	print('==================yolo=============================')
	if OrderItem.objects.filter(product=item, order = order).exists():
		x = OrderItem.objects.get(product=item, order = order)
		print(x)
		x.quantity +=1
		x.save()

	else:
		itemorder, created = OrderItem.objects.get_or_create(
	        product=item,
	        order = order,
	        quantity= 1,

	    )
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_add_to_cart(request, slug):
	order = Order.objects.get(customer=request.user.profile, complete=False)
	item = Product.objects.get(slug=slug)
	items = OrderItem.objects.get(order= order, product=item)
	items.delete()





	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		


def buyNow(request,slug):
	item = Product.objects.get(slug=slug)
	order, created = Order.objects.get_or_create(

		customer=request.user.profile,
		complete=False

    )
	print(order.order_items)
	print('==================yolo=============================')
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

	context={'items' : items, 'order':order,'cartItems':cartItems,'customer':customer}
	return render(request,'checkout.html',context)