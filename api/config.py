from dotenv import load_dotenv
import os

class Config():
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = ""
    JWT_SECRET_KEY = ""
    REDIS_HOST = ""
    REDIS_PORT = 0
    JWT_ACCESS_TOKEN_EXPIRES = 0

load_dotenv()
Config.SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
Config.SECRET_KEY = os.getenv("SECRET_KEY")
Config.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
Config.REDIS_HOST = os.getenv("REDIS_HOST")
Config.REDIS_PORT = int(os.getenv("REDIS_PORT"))
Config.JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))