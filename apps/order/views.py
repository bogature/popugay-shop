
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import *
from rest_framework.views import APIView

from apps.order.models import Order, ItemOrder
from apps.order.serializers import OrderSerializer, ItemOrderSerializer, ItemInfoOrderSerializer
from apps.product.models import Product
from apps.product.serializers import *
from django.core.mail import send_mail, EmailMultiAlternatives

from django.core import mail


User = get_user_model()


class CreateEmailOrder(APIView):

    def post(self, request, pk=None, format=None):
        
        subject, from_email, to = 'Новая заявка на сайте', 'o.bogature@gmail.com', 'o.bogature@gmail.com'
        text_content = ''
        html_content = str(request.data.get('text'))
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response(html_content, status=status.HTTP_201_CREATED)


class CreatelOrder(APIView):

    def post(self, request, pk=None, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateItemOrder(APIView):

    def post(self, request, pk=None, format=None):
        serializer = ItemOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAdminOrders(generics.ListAPIView):
    serializer_class = OrderSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Order.objects.filter(dell=False).order_by('-id')


class GetAdminItemOrders(generics.ListAPIView):
    serializer_class = ItemInfoOrderSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return ItemOrder.objects.filter(order=get_object_or_404(Order, pk=order_id))
