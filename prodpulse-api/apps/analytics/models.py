from django.db import models
from apps.products.models import Product

class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)