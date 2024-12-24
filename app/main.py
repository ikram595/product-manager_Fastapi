from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import  database
from app.database import SessionLocal, engine
from app.models.product import Product
from app.routes.product import productRouter
from app.routes.user import authRouter
from fastapi.middleware.cors import CORSMiddleware 
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi.errors import RateLimitExceeded
from app.seed import seed_data

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

#middlewares
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.state.limiter = limiter

#routes
app.include_router(productRouter, prefix="/products", tags=["products"])
app.include_router(authRouter, prefix="/auth", tags=["authentication"])

database.Base.metadata.create_all(bind=database.engine)#create tables in db
seed_data()#seed data