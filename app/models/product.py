from sqlalchemy import Column, String, Float,Integer, Boolean, ForeignKey
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(String(255), primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Float)
    category = Column(String(255))
    is_favorite = Column(Boolean, default=False)
    user_id = Column(String(255), ForeignKey("users.id"))
