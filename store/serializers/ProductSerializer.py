from rest_framework import serializers
from ..models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price',
            'image1', 'image2', 'image3', 'image4', 'image5', 'main_image'
        ]
