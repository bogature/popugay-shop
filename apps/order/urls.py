
from django.urls import path

from apps.order.views import CreatelOrder, CreateItemOrder, GetAdminOrders, GetAdminItemOrders, CreateEmailOrder

urlpatterns = [

    path('create/', CreatelOrder.as_view()),
    path('create/item/', CreateItemOrder.as_view()),
    path('admin/', GetAdminOrders.as_view()),
    path('admin/item/<int:order_id>/', GetAdminItemOrders.as_view()),

    path('email/', CreateEmailOrder.as_view()),

]