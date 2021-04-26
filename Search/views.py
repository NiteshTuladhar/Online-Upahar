from django.shortcuts import render
from Products.models import *

# Create your views here.
def is_valid_queryparam(param):
    return param!='' and param is not None



def search(request):
    product = Product.objects.all()
    category = Category.objects.all()
    title_query = request.GET.get('q')
    category_query = request.GET.get('category')

    if request.user.is_authenticated:
	    customer = request.user.profile

	    order, created = Order.objects.get_or_create(customer=customer,complete=False)
	    items = order.orderitem_set.all()
	    cartItems = order.get_cart_items

    else:
	    customer = 'Anonymous User'
	    items = []
	    order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
	    cartItems = order['get_cart_items']

    context ={'items' : items, 'order':order,'cartItems':cartItems,'customer':customer,'category':category}

    for z in product:

        if title_query!='' and title_query is not None:

            p = product.filter(product_name__icontains=title_query, category__product_category__icontains=category_query)
            context.update({'queryset':p,
            'cat': category_query,
            })

            if not p:
                context.update({'noresult': 'Sorry you searched nothing matched to the Product',})
        
        if title_query == '' :
            if(category_query !='All Category'):
                p = product.filter(category__product_category__icontains=category_query)
            else:
                p = product.all()

            context.update({'queryset':p,
            'cat': category_query,
            })

    
    

        
    return render(request,'search_result/search.html', context)