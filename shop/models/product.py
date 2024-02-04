from django.db import models

from shop.models import Material
from shop.models.brand import Brand
from shop.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name

    def get_new_price(self):
        return self.price - self.decimal

    def get_old_price(self):
        return self.price

    def has_discount(self):
        return self.decimal != 0
