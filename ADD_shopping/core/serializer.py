from rest_framework import serializers
from core.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'title',
            'price',
            'image',
            'discount',
            'description',
            'status',
            'date_created',
            'unique_id'
            ]
