from django.shortcuts import render
from Products.models import *
from django.utils.crypto import get_random_string
from .models import Payment
import requests


# Create your views here.

def paymentform(request):

    if request.method == 'GET':
        
        reciever_firstname = request.GET['first_name']
        reciever_lastname = request.GET['last_name']
        reciever_email = request.GET['email']
        reciever_address = request.GET['address']
        payment_methods = request.GET['p']

        if request.user.is_authenticated:
            customer = request.user.profile
            order, created = Order.objects.get_or_create(customer=customer,complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_grandtotal':0,'get_cart_total':0,'get_cart_items':0,'shipping':False}
            cartItems = order['get_cart_items']
    unique_id = get_random_string(length=40)
    context={'items' : items, 'order':order,'cartItems':cartItems, 'pid': unique_id}

    if (payment_methods == "ESEWA"):

        return render(request,'payment/esewa.html', context)

    if (payment_methods == "KHALTI"):
        return render(request,'khalti.html', context)



def esewa(request):
    if request.method == 'GET':
        totalAmt = request.GET['amt']
        order = Order.objects.get(id=request.GET['oid'].split('-')[0])
        oid = request.GET['oid']
        refid = request.GET['refId']
        orderitem = OrderItem.objects.get(order_id=order)
        quantity = orderitem.quantity
        productname= orderitem.product

        import xml.etree.ElementTree as ET

        url ="https://uat.esewa.com.np/epay/transrec"
        d = {
        'amt': totalAmt,
        'scd': 'EPAYTEST',
        'rid': refid,
        'pid': oid,
        }

        resp = requests.post(url,d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()
        if status == 'Success':
            payment = Payment(order = order, order_productname=productname, amount=totalAmt, referID = refid, mode = 'ESEWA', quantity=quantity) 
            payment.save()
    context = {

    }
    return render(request, 'payment/success.html', context)

    


