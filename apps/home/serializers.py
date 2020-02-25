
from rest_framework import serializers

from apps.home.models import Home
from apps.product.models import Category, Product


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

