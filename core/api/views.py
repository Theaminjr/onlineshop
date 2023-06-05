from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User,Address
from .serializers import LoginSerializer,SignUpSerializer,ProfileSerializer,AddressSerializer,LoginOtpSerializer,CreateOtpSerializer
from .auth import authenticate_user,decode_jwt,create_otp,validate_otp,create_token,send_email,send_sms



class LoginView(APIView):  
   
    def post(self,request):
        response = LoginSerializer(data=request.data)
        if response.is_valid():
            print(response.validated_data['email'])
            print(response.validated_data['password'])
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



class ProfileView(APIView):
    
    def get(self,request):
        if request.jwt:
            user = User.objects.get(pk=request.jwt['user_id'])
            user = ProfileSerializer(user)
            return Response(user.data)

    
    def put(self, request, format=None):
        user = User.objects.get(id= request.jwt['user_id'])
        serializer = ProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AddressView(APIView):

    def get(self,request):
        user = User.objects.get(id= request.jwt['user_id'])
        addresses = Address.objects.filter(user=user,is_deleted=False)
        addresses = AddressSerializer(addresses,many=True)
        return Response(addresses.data)
    
    def post(self,request):
        user = User.objects.get(id= request.jwt['user_id'])
        address = AddressSerializer(data= request.data)
        if address.is_valid():
           address = Address(location=address.validated_data['location'],user=user)
           address.save()
           return Response({"status":"success"},status=200)
    



class AddressDeleteView(APIView):
    
    def get(self,request,pk):
        user = User.objects.get(id= request.jwt['user_id'])
        address = Address.objects.get(pk=pk)
        if address.is_deleted == False:
           address = AddressSerializer(address)
           return Response(address.data)
        else:
            return Response(status=404)



    def delete(self,request,pk):
        user = User.objects.get(id= request.jwt['user_id'])
        address = Address.objects.get(pk=pk)
        address.delete()
        return Response(status=200)

class CreateOtpView(APIView):

    def post(self,request):
        contact = CreateOtpSerializer(data=request.data)
        if contact.is_valid():
            contact = contact.validated_data["contact"]
            if "@" in contact:
                user = User.objects.get(email=contact)
                if user:
                    otp = create_otp(user.id)
                    print(otp)
                    send_email(user, otp)
                    print(send_email)
                    return Response({"status":"success"},status=200)
            else:
                
                user = User.objects.get(phone_number=contact)
                if user:
                    otp = create_otp(user.id)
                    # send_sms() ارور گیرنده پیامک تبلیغاتی را مسدود کرده
                    print(otp)
                    return Response({"status":"success"},status=200)
            
        return Response({"error":"کاربر وجود ندارد"},status=400)


class LoginOtpView(APIView):

    def post(self,request):
        data = LoginOtpSerializer(data=request.data)
        if data.is_valid():
            contact = data.validated_data["contact"]
            if "@" in contact:
                user = User.objects.get(email=contact)
            else:
                user = User.objects.get(phone_number=contact)
            if user:
                print("error .....")
                if validate_otp(user.id,data.validated_data['otpcode']):
                    token = create_token(user)
                    return Response({"token":token},status=200) 
                else:
                    return Response({"error":"  کد ورودی اشتباه است"},status=400)
            else:
                return Response({"error":"کاربر وجود ندارد"},status=400)