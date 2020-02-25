
from django.urls import path

from apps.product.views import ProductView, GetListAllProduct, GetListAllCategorys, ImageProductView, GetListProduct

urlpatterns = [

    path('categorys/', GetListAllCategorys.as_view()),
    path('all/', GetListAllProduct.as_view()),
    path('<int:pk>/', GetListProduct.as_view()),
    path('info/<int:pk>/', ProductView.as_view()),
    path('image/<int:pk>/', ImageProductView.as_view()),

]