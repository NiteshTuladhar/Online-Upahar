from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from Products.models import Product

class AllProductsList(generics.ListAPIView):

    serializer_class = ProductSerializer


    def get_queryset(self):

        return Product.objects.all()




