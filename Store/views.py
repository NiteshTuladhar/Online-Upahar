from django.shortcuts import render
from Products.models import Product

# Create your views here.
def home(request):

	product = Product.objects.all()

	context = {
		'product': product,
	}

	return render(request,'index.html', context)


def cartpage(request):
	return render(request,'cart.html')

