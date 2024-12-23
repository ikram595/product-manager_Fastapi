import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "ikarMAlee00-key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()
