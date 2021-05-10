from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .token import generatetoken
from Profile.models import Profile
from Products.models import Product,Order, OrderItem, ShippingAdress,Category
from .decorators import unauthenticated_user
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@unauthenticated_user
def userLogin(request):
		
	category = Category.objects.all()

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		check = request.POST.get('check')

		if user is not None:
			login(request, user)
			if check is not None:
				response = HttpResponseRedirect(reverse('Store:homepage'))
				response.set_cookie('email',email)
				response.set_cookie('password',password)
				return response
	
				
			#account = Account.objects.get(id=request.user.id)
			# if account.profile_create is False:
			# 	profile = Profile(user=request.user)
			# 	account.profile_create = True
			# 	profile.save()
			# 	account.save()
			return redirect('Store:homepage')

		else:
			messages.error(request, 'Email or password does not match')
			return redirect("Account:login")
	

	customer = 'Anonymous User'
	items = []
	order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
	cartItems = order['get_cart_items']
	if request.COOKIES.get('email'):	
		context={'items' : items, 'order':order,'cartItems':cartItems, 'customer':customer,'category':category,'email': request.COOKIES.get('email'),'password': request.COOKIES.get('password'),}

		return render (request,'login.html',context)
	else:
		context={'items' : items, 'order':order,'cartItems':cartItems, 'customer':customer,'category':category,}

		return render (request,'login.html',context)
		

	

@unauthenticated_user
def userRegister(request):
	category = Category.objects.all()

	if request.method == 'POST':
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']
		if (len(password) > 6):
			account = Account(email=email, account_name=account_name)
			account.set_password(password)
			try:
				account.token = generatetoken()
				account.save()
				messages.success(request, message="Account created successfully. Please check your email to verify.")
			except:
				messages.error(request, message="Email is already taken or Invalid Email")
			return redirect('Account:login')

		else:
			messages.error(request, message="Password must be greater than 6")
			return redirect('Account:register')
	return render(request,'register.html', context={'category':category})



def userlogout(request):
	logout(request)
	return redirect('Store:homepage')



#Sends Email with token to verify account.

def verifyaccount(request,id,token, backend='django.contrib.auth.backends.ModelBackend'):

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
			login(request, a, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('Store:homepage')
			messages.success(request,"Your account is activated. Hey!! It's a great time to create your profile")

		else:
			messages.error( request,message="Error occured ")

		return render(request,'index.html')

	else:
		messages.success(request,"Your account is already activated. Hey!! It's a great time to create your profile")
		return render(request,'index.html')
	return render(request,'index.html')


def verifypage(request):
	return render(request,'verifypage/verifypage.html')