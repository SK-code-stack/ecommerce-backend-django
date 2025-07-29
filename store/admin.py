from django import forms
from django.contrib import admin
from .models.product import Product
from .models.homeOutdoor import HomePageHomeOutdoor
from .models.homeRecomendedProduct import HomeRecomended
from .models.homeDeals import DealTime, DealProduct
from .models.homeElectronics import HomeElectronics
from .utils.supabase_upload import upload_image_to_supabase


# -------------------- Product Admin --------------------
class ProductAdminForm(forms.ModelForm):
    image1_file = forms.FileField(required=False)
    image2_file = forms.FileField(required=False)
    image3_file = forms.FileField(required=False)
    image4_file = forms.FileField(required=False)
    image5_file = forms.FileField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)

        for i in range(1, 6):
            file_field = self.cleaned_data.get(f'image{i}_file')
            if file_field:
                uploaded_url = upload_image_to_supabase(file_field)  # ✅ Fixed
                setattr(instance, f'image{i}', uploaded_url)

        if commit:
            instance.save()
        return instance


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    search_fields = ['slug']
    readonly_fields = ['slug']
    list_display = ['name', 'category', 'price', 'main_image']
    # exclude = ['image1', 'image2', 'image3', 'image4', 'image5']


# -------------------- Home Outdoor --------------------
@admin.register(HomePageHomeOutdoor)
class HomePageHomeOutdoorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category="Home interiors")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# -------------------- Home Electronics --------------------
@admin.register(HomeElectronics)
class HomePageElectronicAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category="Computer and tech")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# -------------------- Home Recommended --------------------
@admin.register(HomeRecomended)
class HomeRecomendedAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']


# -------------------- Deals --------------------
@admin.register(DealProduct)
class DealProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product']
    list_display = ['product', 'deal', 'discount', 'original_price_display', 'discounted_price_display']

    def original_price_display(self, obj):
        return obj.original_price
    original_price_display.short_description = 'Original Price'

    def discounted_price_display(self, obj):
        return obj.discounted_price
    discounted_price_display.short_description = 'Discounted Price'


@admin.register(DealTime)
class DealTimeAdmin(admin.ModelAdmin):
    list_display = ['deal_start_time', 'deal_ends_at']
