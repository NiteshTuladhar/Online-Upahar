from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .token import generatetoken
from Profile.models import Profile
from .decorators import unauthenticated_user
# Create your views here.
@unauthenticated_user
def userLogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			account = Account.objects.get(id=request.user.id)
			if account.profile_create is False:
				profile = Profile(user=request.user)
				account.profile_create = True
				profile.save()
				account.save()
			return redirect('Store:homepage')

		else:
			messages.error(request, 'Email or password does not match')
			return redirect("Account:login")


	return render (request,'login.html')

@unauthenticated_user
def userRegister(request):
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
	return render(request,'register.html')
@unauthenticated_user
def userlogout(request):
	logout(request)
	return redirect('Account:login')



#Sends Email with token to verify account.

def verifyaccount(request,id,token):

	a = Account.objects.get(id=id)

	if a.is_verified == False:

		if a.token == token:
			a.is_verified = True
			a.save()
			login(request, a)
			return redirect('Store:homepage')
			messages.success(request,"Your account is activated. Hey!! It's a great time to create your profile")

		else:
			messages.error( request,message="Error occured ")

		return render(request,'index.html')

	else:
		messages.success(request,"Your account is already activated. Hey!! It's a great time to create your profile")
		return render(request,'index.html')
	return render(request,'index.html')


