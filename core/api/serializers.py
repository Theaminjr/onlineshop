from core.models import User
from rest_framework import serializers
import re







class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages={'invalid': 'ایمیل نامعتبر',})        
    phone_number = serializers.CharField()
    password = serializers.CharField()
    full_name = serializers.CharField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("این ایمیل پیش از این ثبت نام کرده")
        return value

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("این شماره تماس پیش از این ثبت نام شده")
        if not value.isdigit():
            raise serializers.ValidationError("شماره تماس فقط باید شامل اعداد شود")
        return value

    def validate_password(self, value):
        pattern = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError('پسوورد باید بین ۸ تا ۲۰ عبارت شامل اعداد و حروف انگلیسی باشد')
        return value



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)