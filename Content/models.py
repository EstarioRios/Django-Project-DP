from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    default_image = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - Image"
