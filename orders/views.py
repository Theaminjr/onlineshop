from django.shortcuts import render,HttpResponse,redirect
from products.models import Product
from core.models import User,Address
import json

# Create your views here.
def cart(request):
    if request.jwt:
       products = []
       cart = request.COOKIES.get('cart')
       if cart:
          cart = json.loads(cart)
          for product in cart['products']:
              product = Product.objects.get(id=int(product))
              products.append(product)
       user = User.objects.get(id = request.jwt['user_id'])
       address = Address.objects.filter(user=user,is_deleted=False)
       return render(request, "orders/cart.html",{'products':products,'address':address})
    else:
        return redirect("/users/login")


        

   