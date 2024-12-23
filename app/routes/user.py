from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.crud.user import create_user, get_user_by_email, verify_password
from app.auth import create_access_token
from app.database import get_db

authRouter = APIRouter()

@authRouter.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return  db_user
    except Exception as e:
        print("Error during user registration:", e) 
        raise HTTPException(status_code=400, detail=str(e)) 

@authRouter.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        print("Error during user login") 
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.email})
    return {"message":"successful login","access_token": token, "token_type": "bearer"}
