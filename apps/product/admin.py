
from django.contrib import admin

from apps.product.models import Category, Product, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'money',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'logo',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
