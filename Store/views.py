from django.shortcuts import render, redirect
from Products.models import Product,ProductImage,Order, OrderItem, ShippingAdress, Category, Wishlist, MainCategory,SubCategory
from Profile.models import Profile
from Store.models import SmallBanner
from Cms.models import AboutUs, PrivacyAndPolicy, Banner, TermsAndConditions
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def home(request):
	
	banner_content = Banner.objects.get(id=1)
	product = Product.objects.all()
	product_img = ProductImage.objects.all()
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
		'product_img' : product_img,
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
	category = Category.objects.all()

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

	
	context={'items' : items, 'order':order,'cartItems':cartItems,'customer':customer,'category':category}
	return render(request,'cart.html',context)




def checkoutpage(request):
	category = Category.objects.all()

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

	context={'items' : items, 'order':order,'cartItems':cartItems,'customer':customer,'category':category}
	return render(request,'checkout.html',context)




def categoriesItem(request):
	category = Category.objects.all()
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
		'category':category,

	}

	return render(request,'categories.html',context)




def maincategoriesItem(request,slug):
	category = Category.objects.all()
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
		'subcategory':subcategory,
		'category':category,
		

	}

	return render(request,'category_page/main_category.html',context)



def subcategoriesItem(request,slug):
	category = Category.objects.all()
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

	
	if request.user.is_authenticated:
		customer = request.user.profile
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		total = float(data['form']['total'])

		#order.transaction_id = dtransaction_id

		# if total == order.get_cart_grandtotal:
		# 	order.complete  = True
			
		# 	order.save()
	
		
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
	category = Category.objects.all()
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


	context = {'aboutus_content':aboutus_content,'items' : items, 'order':order,'cartItems':cartItems,'id': id,'customer':customer,'category':category}


	return render(request,'about_us.html', context)



def terms_condition(request):
	category = Category.objects.all()
	tnc_content = TermsAndConditions.objects.get()

	

	context = {'tnc_content':tnc_content,'category':category}

	return render(request,'terms_and_conditions.html',context)



def privacy_policy(request):

	category = Category.objects.all()
	content = PrivacyAndPolicy.objects.get(id=1)


	context = {'content':content, 'category':category}

	return render(request,'privacy_and_policy.html', context)