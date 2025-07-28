from django.contrib import admin
from .models.product import Product
from .models.homeOutdoor import HomePageHomeOutdoor
from .models.homeRecomendedProduct import HomeRecomended
from .models.homeDeals import DealTime, DealProduct
from .models.homeElectronics import HomeElectronics

#  All Products with slug search
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['slug']

#  Home Outdoor filtered by category
@admin.register(HomePageHomeOutdoor)
class HomePageHomeOutdoorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category="Home interiors")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#  Home Electronics filtered by category
@admin.register(HomeElectronics)
class HomePageElectronicAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category="Computer and tech")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#  Home Recomended with product search
@admin.register(HomeRecomended)
class HomeRecomendedAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']

#  Deals and Offers with product search
# Register DealTime and DealProduct in the admin

@admin.register(DealProduct)
class DealProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']
    list_display = ['product', 'deal', 'discount', 'original_price', 'discounted_price']

    def original_price(self, obj):
        return obj.original_price

    def discounted_price(self, obj):
        return obj.discounted_price


@admin.register(DealTime)
class DealTimeAdmin(admin.ModelAdmin):
    list_display = ['deal_start_time', 'deal_ends_at']

