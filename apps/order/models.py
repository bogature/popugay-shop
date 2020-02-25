from django.db import models
from django.contrib.auth import get_user_model
from pytz import unicode

from apps.product.models import Product

User = get_user_model()


class Order(models.Model):
    name = models.CharField(max_length=250)

    phone = models.CharField(max_length=250)

    money = models.FloatField(default=0)

    dell = models.BooleanField(default=False)

    def __str__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    count = models.IntegerField(default=0)

    price = models.FloatField(default=0)

    dell = models.BooleanField(default=False)

    def __str__(self):
        return unicode(self.product)

    class Meta:
        verbose_name = 'Елемент'
        verbose_name_plural = 'Елемент'
