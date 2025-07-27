from django.db import models
from .product import Product
class HomeRecomended(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE, related_name="HomePage_HomeRecomended")

    def __str__(self):
        return self.product.name