from django.shortcuts import render
from Products.models import *
from django.utils.crypto import get_random_string
from Products.models import Product,Order, OrderItem, ShippingAdress
from .models import Payment
from Profile.models import Profile 
import requests

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
import datetime


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
        return render(request,'payment/khalti.html', context)



def esewa(request):
    if request.method == 'GET':
        totalAmt = request.GET['amt']
        order = Order.objects.get(id=request.GET['oid'].split('-')[0])
        oid = request.GET['oid']
        refid = request.GET['refId']

        orderitem = Order.objects.get(id=order.id)


        items = order.orderitem_set.all()
        print(items)
        print('ppppppppppppppppppppp')

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
            payment = Payment(order = order, amount=totalAmt, referID = refid, mode = 'ESEWA')
            payment.save()
<<<<<<< HEAD
    customer = Profile.objects.get(user=request.user)  
    delivery_charge = order.get_cart_total - order.get_cart_total
  

    customer = Profile.objects.get(user=request.user)       
=======


    customer = Profile.objects.get(user=request.user)       

>>>>>>> 2f70609fa159a25aea4f518482429d944504fb03
    context = {
        'items' : items, 'customer': customer,'order' :order, 'dc': delivery_charge,

    }
    return render(request, 'payment/success.html', context)

    

@csrf_exempt
def khalti(request):

    data = request.POST

    token = data["token"]
    amount =data["amount"]
    o_id = data["product_identity"]

    

    print('---------payload data---------------')
    print(token, amount, o_id)
    print('---------------------------------------')

    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
      "token": token,
      "amount": amount
    }
    headers = {
      "Authorization": "Key test_secret_key_6ff60dcc167d4842bf4a84cca67480a9"
    }

    myorder = Order.objects.get(id=o_id)

    items = myorder.orderitem_set.all()

    print('---------my order---------------')
    print(myorder)
    print(items)
    print('---------------------------------------')


    response = requests.post(url, payload, headers = headers)

    print('---------response status---------------')
    print(response)
    print('---------------------------------------')


    resp_dict = response.json()

    print('---------response data---------------')
    print(resp_dict)
    print('-------------------------------------')
    
    if resp_dict.get("idx"):
        payment = Payment(order = myorder,amount=amount, referID = token, mode = 'KHALTI') 
        payment.save()

    else:
        success = False
    
    data = {
        "Success" : True
    }
    return JsonResponse(data)


