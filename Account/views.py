from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def userLogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('Home:homepage')

		else:
			messages.error(request, 'Email or password does not match')
			return redirect("Account:login")


	return render (request,'login.html')


def userRegister(request):
	if request.method == 'POST':
		email = request.POST['email']
		account_name = request.POST['account_name']
		password = request.POST['password']
		if (len(password) > 6):
			account = Account(email=email, account_name=account_name)
			account.set_password(password)
			try:
				account.save()
				messages.success(request, message="Account created successfully")
			except:
				messages.error(request, message="Email is already taken or Invalid Email")
			return redirect('Account:login')

		else:
			messages.error(request, message="Password must be greater than 6")
			return redirect('Account:register')
	return render(request,'register.html')