from .views import LoginView,SignupView
from django.urls import path  



urlpatterns = [  
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),



]  