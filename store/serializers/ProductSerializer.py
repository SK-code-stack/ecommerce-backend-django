from rest_framework import serializers
from ..models.product import Product
from ..models.homeDeals import DealProduct

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'  # or list fields explicitly
        # fields = ['id', 'name', 'price', 'discounted_price', ... other fields]

    def get_discounted_price(self, obj):
        try:
            deal_product = DealProduct.objects.get(product=obj)
            return deal_product.discounted_price
        except DealProduct.DoesNotExist:
            return None  # or return obj.price if you want
