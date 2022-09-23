from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import Product

# Create your views here.

class Productview(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class Cardview(viewsets.ModelViewSet):
    serializer_class = itemcard
    queryset = itemcard.objects.all()

class Contactusview(viewsets.ModelViewSet):
    serializer_class = contact_us
    queryset = contact_us.objects.all()