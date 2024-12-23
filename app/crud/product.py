from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate
from uuid import uuid4

def create_product(db: Session, product_data: dict):
    new_product = Product(**product_data)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: str, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.category = product.category
        db_product.is_favorite = product.is_favorite
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: str):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
