from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
import bcrypt
from uuid import uuid4

def create_user(db: Session, user: UserCreate):
    #check email uniquness
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise Exception(f"Email {user.email} is already in use.")
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(
        id=str(uuid4()), 
        email=user.email, 
        hashed_password=hashed_password.decode('utf-8'),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
