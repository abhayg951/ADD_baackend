from rest_framework import serializers
from core.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'image',
            'brand',
            'item',
            'original_mrp',
            'discounted_mrp', 
            'status',
            'rating',
            'product_details',
            'date_created',
            'slug'
            ]

class carsSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemcard
        fields =[
            'id',
            'pics',
            'brand',
            'original_mrp',
            'discounted_mrp',
            'rating'
        ]