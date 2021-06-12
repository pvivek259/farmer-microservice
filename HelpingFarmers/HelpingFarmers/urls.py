"""HelpingFarmers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from deliveryapp import views 
from deliveryapp.controller import farmercontroller
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FarmerAPIView.as_view(),name='farmer-list'),
    path('primary',views.PrimaryAddressAPIView.as_view(),name='primaryadd-list'),
    path('shipping',views.ShippingAddressAPIView.as_view(),name='shippingadd-list'),

    url(r'createFarmer',farmercontroller.create_farmer),
    url(r'getfarmersJSON',farmercontroller.farmer_list),
    url(r'updateShippingAddressById', farmercontroller.update_shipping_address),
    url(r'addShippingAddressByPhone', farmercontroller.add_shipping_address),
    url(r'getShippingAddressByPhone', farmercontroller.get_shipping_address),
    url(r'getFarmerByPhone',farmercontroller.get_farmer),
]
