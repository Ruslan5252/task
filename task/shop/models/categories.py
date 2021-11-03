from django.db import models

from shop.models.product import Product


class Category(models.Model):
    name = models.CharField(verbose_name='название категории' , max_length=255)
    product = models.ForeignKey(Product , on_delete=models.CASCADE,verbose_name='Товар в категории', max_length=255)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name