from django.shortcuts import render

# Create your views here.
def home(request):

	return render(request,'index.html')


def cartpage(request):
	return render(request,'cart.html')

def contactpage(request):
	return render(request,'contact.html')