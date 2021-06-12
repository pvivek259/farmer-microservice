from rest_framework import serializers

from .models import Farmer,PrimaryAddress,ShippingAddress

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"

class PrimaryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryAddress
        fields = "__all__"

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"