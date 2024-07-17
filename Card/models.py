from django.db import models
from django.contrib.auth.models import User
from Content.models import Product


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def full_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price
