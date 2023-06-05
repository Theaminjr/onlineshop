from django.urls import path
from . import views

urlpatterns=[
path("login/",views.login),
path("logout/",views.logout),
path("login/otp/",views.getotp),
path("signup/",views.signup),
path("profile/",views.profile)
]