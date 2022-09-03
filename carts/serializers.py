from rest_framework import serializers
from .models import Cart,CartItem
from products.serializers import ProdcuctsSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Cart
        fields = '__all__'
class CartItemSerializer(serializers.ModelSerializer):
    cart = serializers.ReadOnlyField(source='cart.id')
    product_data = ProdcuctsSerializer(source='product', read_only=True)
    class Meta:
        model = CartItem
        fields = ('cart','quantity','product','product_data')