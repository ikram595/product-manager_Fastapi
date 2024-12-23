from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.models.product import Product
from app.crud.product import create_product, get_product, update_product, delete_product
from app.database import get_db
from app.auth import get_current_user, require_role
from typing import List
from uuid import UUID, uuid4

from slowapi import Limiter
from slowapi.util import get_remote_address
    
productRouter = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@productRouter.post("/", response_model=ProductResponse)
@limiter.limit("5/minute")
def create_product_route(
                         request:Request,
    
    product: ProductCreate,
                         db: Session = Depends(get_db),
                         current_user: dict = Depends(require_role(["admin"])),# Protected route(only admins)
                         
                         
                         ):
    product_data = product.dict()
    product_data["user_id"] = current_user.id
    product_data["id"]=str(uuid4())
    
    return create_product(db, product_data)

@productRouter.get("/", response_model=List[ProductResponse])
def list_products_route(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Protected route
):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products


@productRouter.get("/{product_id}", response_model=ProductResponse)
def get_product_route(product_id: str,
                      db: Session = Depends(get_db),
                         current_user: dict = Depends(get_current_user)  # Protected route
                      ):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@productRouter.put("/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: str,
                         product: ProductUpdate,
                         db: Session = Depends(get_db),
                         current_user: dict = Depends(require_role(["admin"]))  # Protected route(only admins)
                         ):
    updated_product = update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found or not updated")
    return  updated_product


@productRouter.delete("/{product_id}")
@limiter.limit("3/minute")
def delete_product_route(
                         request:Request,
    
    product_id: str,
                         db: Session = Depends(get_db),
                         current_user: dict = Depends(require_role(["admin"]))  # Protected route(only admins)
                         
                         ):
    deleted_product = delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found or not deleted")
    return {"message": "Product deleted successfully"}

@productRouter.get("/products/favorites", response_model=List[ProductResponse])  
def get_favorite_products(
    db: Session = Depends(get_db), 
    current_user: dict = Depends(get_current_user)  # Protected route
):
    #print ("product.user_id", Product.user_id )
    #print ("current_user id", current_user.id )
    try:
        favorites = (
            db.query(Product)
            .filter(Product.user_id == current_user.id, Product.is_favorite == True)
            .all()
        )
        # for product in favorites:
        #     print(f"Product ID: {product.id}, User ID: {product.user_id}, Is Favorite: {product.is_favorite}")
        return favorites
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
    
