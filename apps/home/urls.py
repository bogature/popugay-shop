from django.conf.urls import url
from django.urls import path

from apps.home import views
from apps.home.views import HomeInfoView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('info/', HomeInfoView.as_view()),
]