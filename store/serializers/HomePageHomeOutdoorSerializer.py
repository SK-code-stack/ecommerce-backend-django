from rest_framework import serializers
from ..models.homeOutdoor import HomePageHomeOutdoor
from .ProductSerializer import ProductSerializer
# home page = HP 
class HPHomeOutdoor(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = HomePageHomeOutdoor
        fields = ["product"]

