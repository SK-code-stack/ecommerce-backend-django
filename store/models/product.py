from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    CATEGORY = [
        ('Chothes and wear', 'CLOTHES AND WARE'),
        ('Home interiors', 'HOME INTERIORS'),
        ('Computer and tech', 'COMPUTER AND TECH'),
        ('Tools and equipment', 'TOOLS AND EQUIPMENT'),
        ('Sport and outdoor', 'SPORT AND OUTDOOR'),
        ('Animal and pets', 'ANIMAL AND PETS'),
        ('Machinery tools', 'MACHINERY TOOLS'),
        ('Others', 'OTHERS'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY, blank=True, null=True)

    # Up to 5 images
    image1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/', blank=True, null=True)
    image5 = models.ImageField(upload_to='products/', blank=True, null=True)

    # main image (select which image is main)
    MAIN_IMAGE_CHOICES = [
        ('image1', 'Image 1'),
        ('image2', 'Image 2'),
        ('image3', 'Image 3'),
        ('image4', 'Image 4'),
        ('image5', 'Image 5'),
    ]
    main_image = models.CharField(max_length=10, choices=MAIN_IMAGE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
