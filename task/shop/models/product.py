from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
