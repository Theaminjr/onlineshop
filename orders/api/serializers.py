from rest_framework import serializers
from ..models import OrderItem,Order
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
     product = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all() )
     class Meta:
        model = OrderItem
        fields = ['product','count']

class OrdersSerializer(serializers.ModelSerializer):

     class Meta:
        model = Order
        fields = ['date','status','price']


class OrderItemsSerializer(serializers.Serializer):
    product= serializers.IntegerField()
    count = serializers.IntegerField()



class CreateOrderSerializer(serializers.Serializer):
    items = OrderItemsSerializer(many=True)
    address = serializers.IntegerField()

# class OrderSerializer(serializers.Serializer):
#     product_id = serializers.IntegerField()
#     count = serializers.IntegerField()