from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


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
    category = models.CharField(max_length=500, choices=CATEGORY, blank=True, null=True)
    productType = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    stock = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    material = models.CharField(max_length=100, blank=True, null=True)
    design = models.CharField(max_length=100, blank=True, null=True)
    customization = models.CharField(max_length=100, blank=True, null=True)
    protection = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=100, blank=True, null=True)
    rating_count = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        null=True,
        blank=True
    )
    verified = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY, blank=True, null=True)

    # Up to 5 images
    image1 = models.URLField(max_length=2000, blank=True, null=True)
    image2 = models.URLField(max_length=2000, blank=True, null=True)
    image3 = models.URLField(max_length=2000, blank=True, null=True)
    image4 = models.URLField(max_length=2000, blank=True, null=True)
    image5 = models.URLField(max_length=2000, blank=True, null=True)

    # main image (select which image is main)
    MAIN_IMAGE_CHOICES = [
        ('image1', 'Image 1'),
        ('image2', 'Image 2'),
        ('image3', 'Image 3'),
        ('image4', 'Image 4'),
        ('image5', 'Image 5'),
    ]
    main_image = models.CharField(max_length=2000, choices=MAIN_IMAGE_CHOICES, blank=True, null=True)

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
