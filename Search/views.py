from django.shortcuts import render
from Products.models import *

# Create your views here.
def is_valid_queryparam(param):
    return param!='' and param is not None



def search(request):
    product = Product.objects.all()
    categories = Category.objects.all()

    title_query = request.GET.get('q')
    category_query = request.GET.get('category')
    context ={}
    if title_query!='' and title_query is not None:
        p = product.filter(product_name__icontains=title_query)
        context.update({'queryset':p,
        'cat': category_query,
        })
    elif product.product_name == title_query and product.category != category_query:
         context.update({'noresult': 'Sorry you searched nothing matched to the Product',})

    if is_valid_queryparam(category_query) and category_query != 'All Category':
        q = product.filter(category__product_category__icontains=category_query)
        context.update({'category':q,})
    

    return render(request,'search_result/search.html', context)