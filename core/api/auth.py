from jose import JWTError, jwt
from django.contrib.auth import authenticate


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"



def decode_jwt(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def authenticate_user(email,password):
    user = authenticate(email=email, password=password)
    if user:
        data = {"user_id":user.id,"is_operator":user.is_operator,"is_productmanager":user.is_productmanager,"is_supervisor":user.is_supervisor}
        token = jwt.encode(data, SECRET_KEY,ALGORITHM)
        return token
    else:
        return None
