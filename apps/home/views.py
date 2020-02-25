from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.home.models import Home
from apps.home.serializers import HomeSerializer


def home(request, path=''):
    context = {

    }
    return render(request, 'index.html', context)


class HomeInfoView(APIView):

    def get_object(self):
        try:
            return Home.objects.all().order_by('-id')[0]
        except Home.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        snippet = self.get_object()
        serializer = HomeSerializer(snippet)
        return Response(serializer.data)