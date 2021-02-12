from django.shortcuts import render, redirect
from Products.models import Product,Order, OrderItem, ShippingAdress, Category, Wishlist, MainCategory,SubCategory
from Profile.models import Profile
from Store.models import SmallBanner
<<<<<<< HEAD
from Cms.models import AboutUs, PrivacyAndPolicy, Banner
=======
<<<<<<< HEAD
from Cms.models import AboutUs, TermsAndConditions
=======
from Cms.models import AboutUs, PrivacyAndPolicy
>>>>>>> aa7ea4b518d2af8acbb78198a9dadceccfc91c92
>>>>>>> 876dddf79c8934409473126b77dcca306e41366e
from django.http import JsonResponse
import json
import datetime
# Create your views here.
def home(request):
	
	banner_content = Banner.objects.get(id=1)
	product = Product.objects.all()
	popular_product = Product.objects.order_by('-visit')
	banner = SmallBanner.objects.all()
	wishlist = Wishlist.objects.all()
	category = Category.objects.all()


	maincategories = MainCategory.objects.all()

	subcategory = SubCategory.objects.all()


	print(subcategory)
	
	id=request.user.id
	if request.user.is_authenticated:
		try:
			if request.user.is_verified == True:
				customer = request.user.profile	
				print(customer)
				order, created = Order.objects.get_or_create(customer=customer,complete=False)
				items = order.orderitem_set.all()
				cartItems = order.get_cart_items
			else:
				return redirect('Account:verifypage')
		except:
			return redirect('Account:verifypage')
	else:
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']



	context = {
		'customer' : customer,
		'product': product,
		'popular_product' : popular_product,
		'banner' : banner,
		'id': id,
		'cartItems' : cartItems,
		'wishlist': wishlist,
		'category' : category,
		'maincategories' : maincategories,
		'subcategory' : subcategory,
		'banner_content': banner_content,
	}

	return render(request,'index.html', context)


def cartpage(request):
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
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	context={'items' : items, 'order':order,'cartItems':cartItems,'customer':customer}
	return render(request,'checkout.html',context)




def categoriesItem(request):
	product = Product.objects.all()
	banner = SmallBanner.objects.all()
	wishlist = Wishlist.objects.all()
	category = Category.objects.all()

	maincategories = MainCategory.objects.all()
	digital_product = SubCategory.objects.filter(category__main_category='Digital Products')

	id=request.user.id
	if request.user.is_authenticated:
		try:
			customer = request.user.profile	
			print(customer)
			order, created = Order.objects.get_or_create(customer=customer,complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		except:
			return redirect('ContactMail:contactpage')
	else:
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	
	context = {
		'customer': customer,
		'product': product,
		'banner' : banner,
		'id': id,
		'cartItems' : cartItems,
		'wishlist': wishlist,
		'category' : category,
		'maincategories' : maincategories,
		'digital_product':digital_product,

	}

	return render(request,'categories.html',context)




def maincategoriesItem(request,slug):
	
	maincategory = MainCategory.objects.get(slug=slug)
	subcategory = SubCategory.objects.all()


	p = Product.objects.filter(subcategory__in=SubCategory.objects.filter(category=MainCategory.objects.get(slug=slug)))

	product_count = p.count()


	wishlist = Wishlist.objects.all()
	


	id=request.user.id
	if request.user.is_authenticated:
		try:
			customer = request.user.profile	
			print(customer)
			order, created = Order.objects.get_or_create(customer=customer,complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		except:
			return redirect('ContactMail:contactpage')
	else:
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	
	context = {
		'customer' : customer,
		'id': id,
		'cartItems' : cartItems,
		'wishlist': wishlist,
		'products' : p,
		'product_count' : product_count,
		'maincategory' : maincategory,
		'subcategory':subcategory
		

	}

	return render(request,'category_page/main_category.html',context)



def subcategoriesItem(request,slug):

	subcategory = SubCategory.objects.get(slug=slug)

	products = Product.objects.filter(subcategory_id=subcategory.id)
	product_count = products.count()

	wishlist = Wishlist.objects.all()
	


	id=request.user.id
	if request.user.is_authenticated:
		try:
			customer = request.user.profile	
			print(customer)
			order, created = Order.objects.get_or_create(customer=customer,complete=False)
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		except:
			return redirect('ContactMail:contactpage')
	else:
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

	
	context = {
		'customer' : customer,
		'id': id,
		'cartItems' : cartItems,
		'wishlist': wishlist,
		'products' : products,
		'product_count' : product_count,
		'subcategory' : subcategory,
		

	}

	return render(request,'category_page/sub_category.html',context)



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



def processOrder(request):

	dtransaction_id = datetime.datetime.now().timestamp()

	data = json.loads(request.body)
	print(data)
	print('datadatadatadatadatadatadatadatadatadatadata')
	
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		total = float(data['form']['total'])

		#order.transaction_id = dtransaction_id

		# if total == order.get_cart_grandtotal:
		# 	order.complete  = True
			
		# 	order.save()
		print('HElloooooooooooooooooooooooooooooooooooooooooo')
		
		ShippingAdress.objects.create(
			customer = customer,
			order = order,
			address = data['shipping']['address'],
			first_name = data['shipping']['first_name'],
			last_name = data['shipping']['last_name'],
			email = data['shipping']['email'],
		)
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print(data['shipping']['address'],data['shipping']['first_name'],)
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	else:
		print('user is not logged in')

	return JsonResponse('payment complete', safe=False)





def aboutUs(request):

	aboutus_content = AboutUs.objects.get()

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


	context = {'aboutus_content':aboutus_content,'items' : items, 'order':order,'cartItems':cartItems,'id': id,'customer':customer}


	return render(request,'about_us.html', context)



def terms_condition(request):

<<<<<<< HEAD
	tnc_content = TermsAndConditions.objects.get()

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


	context = {'tnc_content':tnc_content,'items' : items, 'order':order,'cartItems':cartItems,'id': id,'customer':customer}

	return render(request,'terms_and_conditions.html',context)
=======

	return render(request,'terms_and_conditions.html')
>>>>>>> aa7ea4b518d2af8acbb78198a9dadceccfc91c92



def privacy_policy(request):

	content = PrivacyAndPolicy.objects.get(id=1)
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

	context = {'content':content, 'items' : items, 'order':order,'cartItems':cartItems,'id': id,'customer':customer}

	return render(request,'privacy_and_policy.html', context)