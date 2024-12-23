from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.database import get_db
from app.crud.user import get_user_by_email
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from app.crud.user import get_user_by_email

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
# Create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# Verify JWT token
def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)
                     ):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user

#role checker
def require_role(allowed_roles: list[str]):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="you do not have the necessary permissions")
        return current_user
    return role_checker
