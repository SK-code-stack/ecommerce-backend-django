from django.db import models
from .product import Product
class HomeElectronics(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE, related_name="HomePage_HomeElectroics")

    def __str__(self):
        return self.product.name