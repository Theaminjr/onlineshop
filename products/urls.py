from django.urls import path,include,re_path

from . import views


productspatterns=[
    path("",views.AllProducts.as_view()),
    # path("<int:category>/",views.CategoryList.as_view()),

    re_path(r'^details/(?P<slug>[-\w]+)/', views.ProductDetail.as_view()),
    re_path(r'(?P<slug>[-\w]+)/', views.CategoryList.as_view()),
    path("manager/",views.ProductManager.as_view()),
    
]


urlpatterns = [
    path("products/",include(productspatterns)),
    path("",views.Home.as_view())
]