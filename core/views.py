from django.shortcuts import render,redirect,HttpResponseRedirect

# Create your views here.
def login(request):
    return render(request, "core/login.html")

def getotp(request):
    return render(request, "core/otp.html")

def signup(request):
    return render(request, "core/signup.html")

def profile(request):
    return render(request, "core/profile.html")

def logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie("token")
    return response