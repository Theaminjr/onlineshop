from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateOrderSerializer,OrderItemSerializer,OrdersSerializer
from ..models import OrderItem,Order,Address
from core.models import User
from products.models import Product

class OrderView(APIView):
    
    def get(self,request):
        user = User.objects.get(pk=request.jwt['user_id'])
        orders = Order.objects.filter(user=user)
        orderitems = OrdersSerializer(orders,many=True)
        return Response(orderitems.data)

    def post(self,request):
      if user.jwt:
        orderdetail = CreateOrderSerializer(data=request.data)
        
        if request.jwt:
          user = User.objects.get(id=request.jwt["user_id"])
          order = Order(user=user)
          order.save()
        
        if orderdetail.is_valid(): 
            for orderitem in orderdetail.validated_data['items']:
                product = Product.objects.get(id = orderitem['product'])
                orderitem = OrderItem(product = product,count=orderitem['count'])
                orderitem.save()
                order.items.add(orderitem)
            address = Address.objects.get(id=orderdetail.validated_data['address'])
            order.address = address
            order.save()
        return Response({"status":"success"},status=200)

      else:
        return Response({"status":"error"},status=200)
        
        



class profile(APIView):
    pass