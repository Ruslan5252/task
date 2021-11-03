from django.db import models


class Shop(models.Model):
    name = models.CharField(verbose_name='Название магазина',max_length=255)
    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'
