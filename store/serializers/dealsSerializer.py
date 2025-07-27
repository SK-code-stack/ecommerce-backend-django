from rest_framework import serializers
from ..models.homeDeals import DealsOffers
from .ProductSerializer import ProductSerializer

class HPDeals(serializers.ModelSerializer):
    dealProducts = ProductSerializer()
    original_price = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    discount_percentage = serializers.SerializerMethodField()
    deal_start_time = serializers.DateTimeField()
    deal_ends_at = serializers.DateTimeField()

    class Meta:
        model = DealsOffers
        fields = [
            'dealProducts', 'deal_start_time', 'deal_ends_at', 'discount',
            'original_price', 'discounted_price', 'discount_percentage'
        ]

    def get_original_price(self, obj):
        return obj.original_price

    def get_discounted_price(self, obj):
        return obj.discounted_price

    def get_discount_percentage(self, obj):
        return obj.discount_percentage
