from django.shortcuts import render, redirect
from .models import SellerAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .token import generatetoken
from Profile.models import Profile
from .decorators import unauthenticated_user
# Create your views here.


@unauthenticated_user
def sellerLogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('SellerAccount:sellerdashboard')

		else:
			messages.error(request, 'Email or password does not match')
			return redirect("SellerAccount:sellerlogin")


	return render (request,'seller/login.html')





@unauthenticated_user
def sellerRegister(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']
		address = request.POST['address']
		website = request.POST['website']
		date_of_establishment = request.POST['date_of_establishment']


		if (len(password) > 6):
			account = SellerAccount(email=email, account_name=account_name,first_name=first_name,last_name=last_name,address=address,
								website=website,date_of_establishment=date_of_establishment)
			account.set_password(password)
			print('a')
			try:
				account.token = generatetoken()
				account.save()
				print('b')
				messages.success(request, message="Account created successfully. Please check your email to verify.")
			except:
				messages.error(request, message="Email is already taken or Invalid Email")
			return redirect('SellerAccount:sellerlogin')
			print('c')

		else:
			messages.error(request, message="Password must be greater than 6")
			return redirect('SellerAccount:sellerregister')
			print('d')
	return render(request,'seller/register.html')




#Sends Email with token to verify account.

def verifyaccount(request,id,token):

	a = SellerAccount.objects.get(id=id)

	if a.is_verified == False:

		if a.token == token:
			a.is_verified = True
			a.save()
			login(request, a)
			return redirect('SellerAccount:')
			messages.success(request,"Your account is activated. Hey!! It's a great time to create your profile")

		else:
			messages.error( request,message="Error occured ")

		return render(request,'sellerdashboard.html')

	else:
		messages.success(request,"Your account is already activated. Hey!! It's a great time to create your profile")
		return render(request,'index.html')
	return render(request,'index.html')



def sellerdashboard(request):

	return render(request,'seller/sellerdashboard.html')