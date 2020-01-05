from django.db import models
from product.models import Product

# Create your models here.

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.product.name

    def get_value(self):
        return quantity * price

