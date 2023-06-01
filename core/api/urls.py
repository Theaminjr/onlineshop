from .views import LoginView,SignupView,ProfileView,AddressView,AddressDeleteView,CreateOtpView,LoginOtpView
from django.urls import path  



urlpatterns = [  
    path('login/', LoginView.as_view()),
    path('login/getotp/', CreateOtpView.as_view()),
    path('login/checkotp/', LoginOtpView.as_view()),
    path('signup/', SignupView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('addresses/', AddressView.as_view()),
    path('addresses/<int:pk>', AddressDeleteView.as_view()),



]  