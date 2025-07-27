from django.db import models
from django.core.exceptions import ValidationError
from .product import Product

class DealsOffers(models.Model):
    dealProducts = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="DealsAndOffers")
    deal_start_time = models.DateTimeField(help_text="Start date of the deal", null=True, blank=True)
    deal_ends_at = models.DateTimeField(help_text="Exact end datetime for the deal", null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount in percentage", null=True, blank=True)

    def __str__(self):
        return f"{self.dealProducts.name}"

    @property
    def original_price(self):
        return self.dealProducts.price

    @property
    def discounted_price(self):
        return round(self.original_price * (1 - (self.discount / 100)), 2)

    @property
    def discount_percentage(self):
        return f"{self.discount}%"

    def clean(self):
        # Validation to ensure start time is before end time
        if self.deal_start_time and self.deal_ends_at:
            if self.deal_start_time > self.deal_ends_at.date():
                raise ValidationError("Deal start date cannot be after the deal end date.")
