from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.product.name

    def get_value(self):
        return quantity * price

