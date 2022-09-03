
from django.urls import path
from .views import create_order,get_orders

urlpatterns = [
    path('createorder', create_order),
    path('getorders',get_orders)
]