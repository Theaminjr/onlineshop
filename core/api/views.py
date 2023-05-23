from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User
from .serializers import LoginSerializer,SignUpSerializer
from .auth import authenticate_user,decode_jwt



class LoginView(APIView):  
   
    def post(self,request):
        response = LoginSerializer(data=request.data)
        if response.is_valid():
            token = authenticate_user(email=response.validated_data["email"], password=response.validated_data["password"])
            if token:
                return Response({"token":token},status=200) 

            else:
                return Response({"error":"ایمیل یا پسورد ورودی شما اشتباه است"},status=401)
        return Response({"error":"  ورودی غیر معتبر"},status=401)
            
  
class SignupView(APIView):
    
    def post(self,request):
        response = SignUpSerializer(data=request.data)
        if response.is_valid():
            User.objects.create_user(email = response.validated_data["email"],phone_number = response.validated_data["phone_number"],full_name = response.validated_data["full_name"],password = response.validated_data["password"])
            return Response({"status":"success"},status=200)
        else:
            return Response({"error":response.errors},status=400)



