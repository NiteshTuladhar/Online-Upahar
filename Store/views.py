from django.shortcuts import render
from Products.models import Product,Order, OrderItem, ShippingAdress
from Store.models import SmallBanner
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		customer = request.user.profile
		print(customer)
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []

		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0}
		cardItems = order['get_cart_items']

	product = Product.objects.all()
	banner = SmallBanner.objects.all()
	id=request.user.id

	context = {
		'product': product,
		'banner' : banner,
		'id': id,
		'cartItems' : cartItems
	}

	return render(request,'index.html', context)


def cartpage(request):
	if request.user.is_authenticated:
		customer = request.user.profile
		print(customer)
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order['get_cart_items']
		print(items)
	else:
		items = []

		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']


	context={'items' : items, 'order':order,'cartItems':cartItems}
	return render(request,'cart.html',context)




def checkoutpage(request):
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

		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0}
		cartItems = order['get_cart_items']


	context={'items' : items, 'order':order,'cartItems':cartItems}
	return render(request,'checkout.html',context)



def updateItem(request): 

	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:',action)
	print('Product:',productId)

	customer = request.user.profile
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer,complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity+1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity-1)

	orderItem.save()

	if orderItem.quantity <=0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)