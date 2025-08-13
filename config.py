from dotenv import load_dotenv
import os

load_dotenv()

key_secret=os.getenv('SECRET_KEY')
algor=os.getenv('ALGORITHM')
ate= int(os.getenv("ACCESS_TOKEN_EXPIRE","30"))

# api ด้านนอก
Base_URL=os.getenv('Base_URL')
Apikey=os.getenv('Apikey')
Authorization=os.getenv('Authorization')
Content_type=os.getenv('Content_Type')