from django.db import models
from django.core.exceptions import ValidationError
from .product import Product  # adjust import if needed


class DealTime(models.Model):
    deal_start_time = models.DateTimeField(help_text="Start time of the deal")
    deal_ends_at = models.DateTimeField(help_text="End time of the deal")



    def clean(self):
        if self.deal_start_time and self.deal_ends_at:
            if self.deal_start_time > self.deal_ends_at:
                raise ValidationError("Start time cannot be after end time.")
    def save(self, *args, **kwargs):
        if not self.pk and DealTime.objects.exists():
            raise ValidationError("Only one DealTime instance is allowed.")
        super().save(*args, **kwargs)


class DealProduct(models.Model):
    deal = models.ForeignKey(DealTime, on_delete=models.CASCADE, related_name='deal_products')
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=5, decimal_places=2, help_text="Discount for this product")

    def __str__(self):
        return f"{self.product.name} - {self.discount}%"

    @property
    def original_price(self):
        return self.product.price

    @property
    def discounted_price(self):
        return round(self.original_price * (1 - (self.discount / 100)), 2)

    @property
    def discount_percentage(self):
        return f"{self.discount}%"
