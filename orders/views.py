from django.shortcuts import render,HttpResponse

# Create your views here.
def operatorpanel(request):
    return render(request, "orders/manager.html")