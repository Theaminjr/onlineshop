from jose import JWTError, jwt
from django.contrib.auth import authenticate
import functools
import random
import redis
from django.core.mail import send_mail
from kavenegar import *




redis_client = redis.Redis(host='localhost', port=6379, db=0)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


class JwtMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print("********************************")
        token = request.COOKIES.get('token') 
        if token:
            request.jwt = decode_jwt(token)
        else:
            request.jwt = None
        response = self.get_response(request)
        return response



def decode_jwt(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def authenticate_user(email,password):
    user = authenticate(username=email, password=password)
    if user:
        return create_token(user)
    else:
        return None


def create_token(user):
        data = {"user_id":user.id,"is_operator":user.is_operator,"is_productmanager":user.is_productmanager,"is_supervisor":user.is_supervisor}
        token = jwt.encode(data, SECRET_KEY,ALGORITHM)
        return token


def create_otp(user_id):
    code = random.randint(1000, 9999)
    redis_client.set(name=f"{user_id}", value=f"{code}", ex=180)
    return code

def validate_otp(user_id, otp):
  key = f'{user_id}'
  stored_otp = redis_client.get(key)
  if stored_otp is None:
    return False
  if stored_otp.decode('utf-8') != otp:
    return False
  redis_client.delete(key)
  return True


def send_email(user,code):
    send_mail(
    'کد ورود',
    f'کد ورود شما.{code}',
    "noucampmaktab@gmail.com",
    [f'{user.email}'],
    fail_silently=False,
)
def send_sms():
    try:
      api = KavenegarAPI('584F65506F34446364466337334B6273694C363352497056653638513448346E784F58743036595470544D3D')
      params = { 'sender' : '10008663', 'receptor': '0912', 'message' :'تست '}
      response = api.sms_send( params)
    except APIException as e: 
       print(e)
    except HTTPException as e: 
       print(e)
