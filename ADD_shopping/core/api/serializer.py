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
            'mrp',
            'discount_Percentage', 
            'status',
            'rating',
            'product_details',
            'date_created',
            'slug'
            ]

