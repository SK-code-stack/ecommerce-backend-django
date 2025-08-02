from django.shortcuts import render
from rest_framework.decorators import api_view
# Models 
from .models.product import Product
from .models.homeOutdoor import HomePageHomeOutdoor
from .models.homeElectronics import HomeElectronics
from .models.homeRecomendedProduct import HomeRecomended
from .models.homeDeals import DealProduct, DealTime
# serializers of home page  starts with HP home page 
from .serializers.ProductSerializer import ProductSerializer
from .serializers.HomePageHomeOutdoorSerializer import HPHomeOutdoor
from .serializers.homeElectronicsSerializer import HPhomeElectronics
from .serializers.homeRecomendedSerializer import HPhomeRecomended
from .serializers.dealsSerializer import HPDealsSerializer

from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def product(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
    


#  home page home and outdoor products
@api_view(['GET'])
def homePage_homeOutdoor(request):
    product = HomePageHomeOutdoor.objects.filter(product__category="Home interiors")[:8]
    serializer = HPHomeOutdoor(product, many=True)
    return Response(serializer.data)


#  home page Electronics
@api_view(['GET'])
def homePage_electronics(request):
    product = HomeElectronics.objects.filter(product__category="Computer and tech")[:8]
    serializer = HPhomeElectronics(product, many=True)
    return Response(serializer.data)



#  home page Recomended
@api_view(['GET'])
def homePage_recomended(request):
    product = HomeRecomended.objects.all()
    serializer = HPhomeRecomended(product, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def home_deals(request):
    deals = DealTime.objects.all()
    serializer = HPDealsSerializer(deals, many=True)
    return Response(serializer.data)


# prodct detail using slug
@api_view(['GET'])
def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'detail': 'Product not found.'}, status=404)










