from rest_framework import serializers
from ..models.homeDeals import DealTime, DealProduct
from .ProductSerializer import ProductSerializer


class DealProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    original_price = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = DealProduct
        fields = [
            'product', 'discount',
            'original_price', 'discounted_price', 'discount_percentage'
        ]

    def get_original_price(self, obj):
        return obj.original_price

    def get_discounted_price(self, obj):
        return obj.discounted_price

    def get_discount_percentage(self, obj):
        return obj.discount_percentage


class HPDealsSerializer(serializers.ModelSerializer):
    deal_products = DealProductSerializer(many=True, read_only=True)

    class Meta:
        model = DealTime
        fields = ['deal_start_time', 'deal_ends_at', 'deal_products']
