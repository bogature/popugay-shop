
from django.db import models
from django.contrib.auth import get_user_model
from pytz import unicode

User = get_user_model()


class Category(models.Model):

    name = models.CharField(max_length=250)

    def __str__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'


class Product(models.Model):

    title = models.CharField(max_length=500, null=True, blank=True)

    description = models.CharField(max_length=500, null=True, blank=True)

    keywords = models.CharField(max_length=500, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    logo = models.ImageField('Logo', null=True, blank=True, upload_to='profile_images')

    name = models.CharField(max_length=250)

    text = models.TextField()

    money = models.FloatField(default=0)

    def __str__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class Image(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    logo = models.ImageField('Logo', null=True, blank=True, upload_to='profile_images')

    def __str__(self):
        return unicode(self.id)

    class Meta:
        verbose_name = 'Фото для продуктов'
        verbose_name_plural = 'Фото для продуктов'
