
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import generics
from rest_framework.pagination import *
from rest_framework.views import APIView

from apps.product.models import Product
from apps.product.serializers import *

User = get_user_model()


class GetListAllCategorys(generics.ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Category.objects.all()


class GetListAllProduct(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Product.objects.all().order_by('-id')


class ImageProductView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Image.objects.filter(product_id=pk)


class GetListProduct(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(category_id=pk).order_by('-id')


class ProductView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)