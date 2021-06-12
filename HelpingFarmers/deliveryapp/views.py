from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Farmer,ShippingAddress,PrimaryAddress
from .serializers import FarmerSerializer,ShippingAddressSerializer,PrimaryAddressSerializer
#to create farmer having primary address and other meta data
class FarmerAPIView(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class PrimaryAddressAPIView(generics.ListCreateAPIView):
    queryset = PrimaryAddress.objects.all()
    serializer_class = PrimaryAddressSerializer

class ShippingAddressAPIView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
