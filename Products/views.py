from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Profile.models import Profile
from .models import Product

# Create your views here.


def productDetails(request,slug):

	details = Product.objects.get(slug=slug)
	
	context = {

		'details' : details
	}

	return render(request,'product_details/product_details.html',context)