
from django.db import models
from django.contrib.auth import get_user_model
from pytz import unicode

User = get_user_model()


class Home(models.Model):

    logo = models.ImageField('logo', null=True, blank=True, upload_to='logo_images')

    slider = models.ImageField('slider', null=True, blank=True, upload_to='slider_images')

    name = models.CharField(max_length=250)

    text_top = models.TextField()

    text = models.TextField()

    email = models.CharField(max_length=200, null=True, blank=True)

    phone = models.CharField(max_length=200, null=True, blank=True)

    location = models.CharField(max_length=200, null=True, blank=True)

    time = models.CharField(max_length=200, null=True, blank=True)

    facebook = models.CharField(max_length=200, null=True, blank=True)

    instagram = models.CharField(max_length=200, null=True, blank=True)

    vk = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
