from sqlalchemy import Column, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(String(255), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(50), default="user")
