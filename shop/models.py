from django.db import models
from cloudinary.models import CloudinaryField   # ✅ استيراد CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField("image", folder="categories", blank=True, null=True)  # ✅ صورة من Cloudinary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = CloudinaryField("image", folder="products", blank=True, null=True)  # ✅ صورة من Cloudinary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
