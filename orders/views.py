from carts.models import Cart,CartItem
from user.utils import get_user
from rest_framework.decorators import api_view
from .models import Orders,OrderItems
from django.http.response import JsonResponse
from rest_framework import status
from .models import Orders,OrderItems
from .serializers import OrderSerializer
# Create your views here.

@api_view(['POST'])
def create_order(request):
    user_id = get_user(request)
    if request.method == 'POST':
        cart_instance = Cart.objects.filter(user=user_id).first()
        cart_items = CartItem.objects.filter(cart=cart_instance)
        if len(cart_items) == 0:
            return JsonResponse({"message":"Cart is empty"},status=status.HTTP_422_UNPROCESSABLE_ENTITY,safe=False)
        
        order_instance = Orders.objects.create(user=user_id)         
        for item in cart_items:
            order_item = OrderItems.objects.create(order=order_instance,product=item.product,quantity=item.quantity)
        cart_items.delete()
        return JsonResponse({"message":"order created"},status=status.HTTP_201_CREATED,safe=False)
    
@api_view(['GET'])  
def get_orders(request):
    user_id = get_user(request)
    if request.method == 'GET':
        order_items = Orders.objects.filter(user=user_id)
        order_serializer = OrderSerializer(order_items, many=True)
        return JsonResponse(order_serializer.data, safe=False)
        