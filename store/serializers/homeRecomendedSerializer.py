from rest_framework import serializers
from ..models.homeRecomendedProduct import HomeRecomended
from .ProductSerializer import ProductSerializer

class HPhomeRecomended(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = HomeRecomended
        fields = ["product"]