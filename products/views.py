from django.shortcuts import render,HttpResponse
from .models import Product
from django.views import View
from django.views.generic import ListView
from .forms import CreateProduct

# Create your views here.


class Home(View):
    def get(self,request):
        return render(request, 'products/home.html')



class AllProducts(ListView):
    paginate_by = 4
    model = Product

class ProductManager(View):
    def get(self,request):
        createform = CreateProduct()
        return render(request, "products/manager.html",{"createform":createform})
    def post(self,request):
        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks")



