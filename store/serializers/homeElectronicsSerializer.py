from rest_framework import serializers
from ..models.homeElectronics import HomeElectronics
from .ProductSerializer import ProductSerializer

class HPhomeElectronics(serializers.ModelSerializer):
    product = ProductSerializer()  # <-- Add parentheses here

    class Meta:
        model = HomeElectronics
        fields = ["product"]
