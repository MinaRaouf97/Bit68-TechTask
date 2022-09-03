
from django.urls import path
from .views import get_create_cart,add_get_cart

urlpatterns = [
    path('cart', get_create_cart),
    path('additem',add_get_cart),
    
    

]