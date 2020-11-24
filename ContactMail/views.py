from django.shortcuts import render, redirect
from .mail import CustomMail
from django.contrib import messages

from Products.models import Product,Order, OrderItem, ShippingAdress

# Create your views here.
def contactpage(request):

    if request.user.is_authenticated:
        customer = request.user.profile
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        print(items)
    else:
        items = []
        order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']

    context={'items' : items, 'order':order,'cartItems':cartItems}

    return render(request,'contact.html', context)

def mailsend(request):
    if request.method == 'POST':
        hostemail = 'sushek69@gmail.com'
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjects = request.POST.get('subject')
        number = request.POST.get('phone')
        textmessage = request.POST.get('message')
        mail = CustomMail('mail/email_template.html', 'From Website Mail Notification', [hostemail,], nameofcustomer=name, numberofcustomer=number, messageofcustomer=textmessage, emailofcustomer=email, subjects=subjects)
        mail.push()
        messages.success(request, message="Mail sent successfully")
        return render(request, 'Store:homepage')

    else:
        messages.error(request, message="Sorry couldn't send mail")
        return redirect('ContactMail:contactpage')