from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .token import generatetoken
# Create your views here.
def userLogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('Store:homepage')

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



#Sends Email with token to verify account.

def verifyaccount(request,id,token):

	a = Account.objects.get(id=id)

	if a.is_verified == False:

		if a.token == token:
			a.is_verified = True
			a.save()
			login(request, a)
			return redirect('Home:homepage')
			messages.success(request,mark_safe("Your account is activated. Hey!! It's a great time to <a href="" >create your profile.</a>"))#mark_safe is used to allow link in a messages

		else:
			messages.error( request,message="Error occured ")

		return render(request,'index.html')

	else:
		messages.success(request,mark_safe("Your account is already activated. Hey!! It's a great time to <a href="">create your profile.</a>"))
		return render(request,'index.html')
	return render(request,'index.html')

def profile_edit(request):
	images = request.FILES['image']
	print(images)
	user_id = request.user.id
	acc = Account.objects.get(id=user_id)
	acc.image = images
	acc.save()
	print('Done')
	return redirect('Account:userprofile')
