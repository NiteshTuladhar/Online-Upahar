from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Profile
from Account.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import ProfileEdit 
# Create your views here.
def userProfile(request):
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


def profile_edit(request):
	images = request.FILES.get('image')
	print(images)
	profile = Profile.objects.get(user__id=request.user.id)
	profile.profile_image = images
	profile.save()
	print('Done')
	return redirect('Profile:userprofile')


def completeuserprofile(request):

    userinfo = Profile.objects.get(user_id=request.user.id)
    print(userinfo.first_name)
    user_info = Account.objects.get(id=request.user.id)

    return render(request,'userprofile/display_profile.html',context={'userinfo':userinfo, 'user_info': user_info})