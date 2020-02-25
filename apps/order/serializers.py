
from rest_framework import serializers

from apps.order.models import Order, ItemOrder
from apps.product.models import Category, Product
from apps.product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = '__all__'


class ItemInfoOrderSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True, many=False)


    class Meta:
        model = ItemOrder
        fields = '__all__'

