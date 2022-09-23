from rest_framework import serializers
from core.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'image',
            'brand',
            'item',
            'mrp',
            'discount_Percentage', 
            'status',
            'rating',
            'product_details',
            'date_created',
            'slug'
            ]


class itemcardser(serializers.ModelSerializer):
    class Meta:
        model = itemcard
        fields = [
            'image',
            'brand',
            'mrp'
        ]


class contactus(serializers.ModelSerializer):
    class Meta:
        model = contact_us
        fields = [
            'name'
        ]