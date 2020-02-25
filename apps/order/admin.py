
from django.contrib import admin

from apps.order.models import Order, ItemOrder

admin.site.register(Order)
admin.site.register(ItemOrder)
