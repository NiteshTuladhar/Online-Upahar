from django.db import models
from Products.models import Order
from datetime import datetime, timezone

payment_methods = [
   ("ESEWA","ESEWA"),
    ("KHALTI", "KHALTI")
]
# Create your models here.

class Payment(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_productname = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(decimal_places=3, max_digits=10)
    referID = models.CharField(max_length=100)
    mode = models.CharField(choices=payment_methods, max_length=15)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(max_length=10, null=True)