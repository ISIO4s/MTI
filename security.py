from fastapi import APIRouter, Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jose import JWTError,jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta
from typing import Optional

secret_key = "maximus"
algorithm = "HS256"
time =  60 * 24 

rounter = APIRouter(
    prefix="/MTIPRB",
    tags=["MTIPRB"]
)
pwd = CryptContext(schemes=["bcrypt"],deprecated ="auto")
oauth = OAuth2PasswordBearer(tokenUrl="token")

Master ={
    "MITPRB":{
                "username":"MITPRB",
                "password":pwd.hash("PRBMIT"),
                "disabled":False
            },
    "JOHN":{
                "username":"JOHN",
                "password":pwd.hash("SMITE"),
                "disabled":False
            }
}
def create_token(data: dict, expires_token:Optional[timedelta] = None):
    copy = data.copy()
    if expires_token:
        expire = datetime.utcnow() + expires_token
        print("เริ่มต้นการงาน")
        print(expire)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        print("เริ่มต้นการงาน")
        print(expire)
    copy.update({"exp":expire})
    token = jwt.encode(copy,secret_key,algorithm=algorithm)
    return token
def password_verify(loginpassword,hashpassword):
    return pwd.verify(loginpassword,hashpassword)
def user_verify(user:str):
    username = Master.get(user)
    if username:
        return username
    else: 
        return None
def auth(username: str,password:str):
    user = user_verify(username)
    if not user or not password_verify(password,user["password"]):
        return False
    return user
def get_current_time(token:str = Depends(oauth)):
    try:
        result = jwt.decode(token,secret_key,algorithms=algorithm)
        expiretime = result.get("exp")
        time = datetime.utcfromtimestamp(expiretime)
        now = datetime.utcnow()
        remain = time - now
        
        return remain
    except Exception as ex:
        return ex
def get_current_user(token:str = Depends(oauth)):
    try:
        result = jwt.decode(token,secret_key,algorithms=algorithm)
        username:str = result.get("sub")
        if not username:
            raise HTTPException(
           status_code = status.HTTP_401_UNAUTHORIZED,
           detail ="UNAUTHORIZED"
       )
        return username
        return result
    except JWTError:
        raise HTTPException(
           status_code = status.HTTP_401_UNAUTHORIZED,
           detail ="UNAUTHORIZED"
       )
@rounter.post("/Space")
def spance(current_user:str = Depends(get_current_time)):
    print(current_user)
    return current_user

@rounter.post("/to")
def log(current_user:str = Depends(get_current_user)):
    return current_user

@rounter.post("/token")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
   result = auth(form_data.username,form_data.password)

   if not result:
      raise HTTPException(
           status_code = status.HTTP_401_UNAUTHORIZED,
           detail ="UNAUTHORIZED"
       )
   access_token_time = timedelta(minutes = time)
   access_token = create_token(
       data={"sub":result["username"]},
       expires_token=access_token_time)
   return access_token