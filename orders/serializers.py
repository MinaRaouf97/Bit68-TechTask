from rest_framework import serializers
from .models import Orders,OrderItems
from user.serializers import UserSerializer


class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = orderItemSerializer(source="orderitems",many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Orders
        fields = [
            'user',
            'created_at',
            'order_items'
        ]



