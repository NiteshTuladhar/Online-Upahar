from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from Account.models import Account
from Products.models import Order, OrderItem, Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import ProfileEdit 
# Create your views here.
def userProfile(request):

	category = Category.objects.all()

	if request.method == 'GET':
		userinfo = Account.objects.get(id=request.user.id)
		profile = Profile.objects.get(user_id=request.user.id)

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

		context={'items' : items, 'order':order,'cartItems':cartItems,'profile' : profile,'userinfo' : userinfo,'customer':customer,'category':category}

		return render(request,'userprofile/profile.html',context)

	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		phone = request.POST['phone']
		mobile = request.POST['mobile']
		gender = request.POST['gender']
		location = request.POST.get('location')


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
				messages.success(request, message="Your profile is set.")
				return redirect('Profile:completeuserprofile')
			except:
				messages.error(request, message="Error occured")
		
			return redirect('Profile:userprofile')

	

	return render(request,'userprofile/profile.html')


def profile_edit(request):
	images = request.FILES.get('image')
	print(images)
	profile = Profile.objects.get(user__id=request.user.id)
	profile.profile_image = images
	profile.save()
	print('Done')
	return redirect('Profile:userprofile')


def completeuserprofile(request):

	context = {}

	userinfo = Profile.objects.get(user_id=request.user.id)
	print(userinfo.first_name)
	user_info = Account.objects.get(id=request.user.id)

	

	if request.user.is_authenticated:
		
		category = Category.objects.all()

		customer = request.user.profile
		print(customer)
		order, created = Order.objects.get_or_create(customer=customer,complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		print(items)
		

		
		myorders = Order.objects.filter(customer=request.user.profile, complete=True)

		print('------------------------myorders--------------')
		print(myorders)
		print('------------------------myorders--------------')

		all_orders = []

		for order in myorders:

			myorder_items = OrderItem.objects.filter(order_id=order.id)
			print('[[[[[[[[[[[[[[[[[[[[[[')
			all_orders.append(myorder_items)
			print('[[[[[[[[[[[[[[[[[[[[[[')
			print(myorder_items)
			print('--------------------------------')

		print('++++++++++++++all orders+++++++++++++++++++')
		print(all_orders)
		print('++++++++++++++all orders+++++++++++++++++++')
		
		total_items = []

		for item in all_orders:
			for i in item:
				total_items.append(i)		

		print(total_items)
		print('==========================================')
			
		context.update({'items' : items, 'order':order,'cartItems':cartItems,'userinfo' : userinfo,'customer':customer,'total_items':total_items,'category':category})

		
	else:
		customer = 'Anonymous User'
		items = []
		order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
		cartItems = order['get_cart_items']

		context={'items' : items, 'order':order,'cartItems':cartItems,'userinfo' : userinfo,'customer':customer,'category':category}

	return render(request,'userprofile/display_profile.html',context)






def sellerProfile(request):
	if request.method == 'GET':
		userinfo = Account.objects.get(id=request.user.id)
		profile = Profile.objects.get(user_id=request.user.id)
		form = ProfileEdit(request.GET or None,instance=profile)
		context = {
			'profile' : profile,
			'userinfo' : userinfo,
			'form' : form
		}
		return render(request,'userprofile/profile.html',context)

	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		phone = request.POST['phone']
		mobile = request.POST['mobile']
		gender = request.POST['gender']
		location = request.POST.get('location')
		print(location)

		p = Profile.objects.get(user_id=request.user.id)
		if request.method == 'POST':
			profile = ProfileEdit(request.POST or None,instance=p)
			data=profile.save(commit=False)
			data.user=request.user
			try:
				data.save()
				messages.success(request, message="Your profile is set.")
				return redirect('Profile:completeuserprofile')
			except:
				messages.error(request, message="Error occured")
			return redirect('Profile:userprofile')


	return render(request,'userprofile/profile.html')