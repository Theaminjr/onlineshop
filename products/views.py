from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Category
from django.views import View
from django.views.generic import ListView,DetailView
from .forms import CreateProduct


# Create your views here.

def get_subcategories(category):
        subcategories = []
        for subcategory in category.children.all():
           subcategories.append(subcategory)
           subcategories += get_subcategories(subcategory)
        return subcategories


class Home(View):

    def get(self,request):
        recent = Product.objects.all()
        recommended = Product.objects.filter(recommended=True)
        return render(request, 'products/home.html',{"recent":recent[0:5],"recommended":recommended})




class AllProducts(ListView):
    paginate_by = 8
    model = Product

    def get_context_data(self,**kwargs):
       context = super(AllProducts,self).get_context_data(**kwargs)
       context['categories'] = Category.objects.filter(parent=None)
       return context


class CategoryList(ListView):
    paginate_by = 8
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        all_products= []
        # parent = Category.objects.get(pk=self.kwargs["category"])
        parent = Category.objects.get(slug=self.kwargs["slug"])
        subcategories = get_subcategories(parent)
        subcategories.append(parent) 
        queryset = Product.objects.filter(category__in=subcategories)
        return queryset

    def get_context_data(self,**kwargs):
       context = super(CategoryList,self).get_context_data(**kwargs)
    #    parent = Category.objects.get(pk=self.kwargs["category"])
       parent = Category.objects.get(slug=self.kwargs["slug"])
       context['categories'] = parent.children.all()
       return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


class ProductManager(View):
    def get(self,request):
        createform = CreateProduct()
        return render(request, "products/manager.html",{"createform":createform})
    def post(self,request):
        form = CreateProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks")



