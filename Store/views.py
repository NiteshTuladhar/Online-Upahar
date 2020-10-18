from django.shortcuts import render
from Products.models import Product
from Store.models import SmallBanner

# Create your views here.
def home(request):

	product = Product.objects.all()
	banner = SmallBanner.objects.all()
	id=request.user.id

	context = {
		'product': product,
		'banner' : banner,
		'id': id,
	}

	return render(request,'index.html', context)


def cartpage(request):
	return render(request,'cart.html')


