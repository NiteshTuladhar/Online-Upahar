from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from Account.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def userProfile(request):
	if request.method == 'GET':
		userinfo = Account.objects.get(id=request.user.id)
		profile = Profile.objects.get(user_id=request.user.id)
		return render(request,'userprofile/profile.html',context={'userinfo':userinfo, 'profile': profile})

	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		phone = request.POST['phone']
		mobile = request.POST['mobile']
		gender = request.POST['gender']
		location = request.POST.get('location')
		profile = Profile(first_name=first_name, last_name=last_name,phone=phone,mobile=mobile,gender=gender,location=location)
		try:
			profile.save()
			messages.success(request, message="Your profile is set.")
			return redirect('Store:homepage')
		except:
			messages.error(request, message="Error occured")
		return redirect('Profile:userprofile')

	return render(request,'userprofile/profile.html')


def profile_edit(request):
	images = request.FILES['image']
	print(images)
	profile = Profile.objects.get(user__id=request.user.id)
	profile.profile_image = images
	profile.save()
	print('Done')
	return redirect('Profile:userprofile')