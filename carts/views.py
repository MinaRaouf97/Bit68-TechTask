from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from django.http.response import JsonResponse
from user.utils import get_user
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status




# Create your views here.
@api_view(['GET','POST'])
def get_create_cart(request,*args):
    pk =  get_user(request)
    if request.method == 'GET':
        cart = Cart.objects.filter(user=pk)
        cart_serializer = CartSerializer(cart,many=True)
        return JsonResponse(cart_serializer.data,safe=False)
    elif request.method == 'POST':
        pass

@api_view(['POST','GET'])
def add_get_cart(request):
    user_id = get_user(request)
    if request.method == 'POST':
        cart_instance = Cart.objects.filter(user=user_id).first()
        cart_item_data = JSONParser().parse(request)
        cart_item_serializer = CartItemSerializer(data=cart_item_data)
        if cart_item_serializer.is_valid():
            cart_item_serializer.save(cart=cart_instance)
            return JsonResponse(cart_item_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cart_item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        cart_instance = Cart.objects.filter(user=user_id).first()
        cart_items  = CartItem.objects.filter(cart=cart_instance.id)
        cart_items_serializer = CartItemSerializer(cart_items, many=True)
        return JsonResponse(cart_items_serializer.data, safe=False)


        
        
    