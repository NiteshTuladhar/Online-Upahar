from Products.models import Product,ProductImage,Order, OrderItem, ShippingAdress, Category, Wishlist, MainCategory,SubCategory

def cartitemcount(request):
    if request.user.is_authenticated: 
	    customer = request.user.profile
	    print('from context processorrrr------------------------------------------------')
	    order, created = Order.objects.get_or_create(customer=customer,complete=False)
	    items = order.orderitem_set.all()
	    cartItems = order.get_cart_items
	    print(items)
    else:
        customer = 'Anonymous User'
        items = []
        order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    return {
        'items' : items, 'order':order,'cartItems':cartItems,'id': id,'customer':customer,
    }
