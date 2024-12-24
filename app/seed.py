from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.user import User
from uuid import uuid4
from app.database import SessionLocal
from app.crud.user import create_user
from app.crud.product import create_product
from app.schemas.user import UserCreate


def seed_data():
    db = SessionLocal()
    try:
        user1_data = UserCreate(email="user1@solyntek.com", password="123456")
        user2_data = UserCreate(email="user2@solyntek.com", password="234567")
        admin_data = UserCreate(email="admin@solyntek.com", password="234567",role="admin")
#create users& products
        user1 = create_user(db, user1_data)
        user2 = create_user(db, user2_data)
        admin = create_user(db, admin_data)
        
        create_product(db, {"id": str(uuid4()), "name": "Product 1", "description": "Description for Product 1", "price": 100.0, "category": "Electronics", "is_favorite": False, "user_id": user1.id})
        create_product(db, {"id": str(uuid4()), "name": "Product 2", "description": "Description for Product 2", "price": 200.0, "category": "Food", "is_favorite": False, "user_id": user2.id})
        create_product(db, {"id": str(uuid4()), "name": "Product 3", "description": "Description for Product 3", "price": 150.0, "category": "Books", "is_favorite": False, "user_id": admin.id})
        create_product(db, {"id": str(uuid4()), "name": "book1", "description": "Description for book1", "price": 150.0, "category": "Books", "is_favorite": False, "user_id": admin.id})

        print("Seed data added successfully!")
    finally:
        db.close()

