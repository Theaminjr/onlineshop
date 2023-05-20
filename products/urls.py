from django.urls import path,include
from . import views


productspatterns=[
    path("",views.AllProducts.as_view()),
    path("manager",views.ProductManager.as_view())
]


urlpatterns = [
    path("products/",include(productspatterns)),
    path("",views.Home.as_view())
]