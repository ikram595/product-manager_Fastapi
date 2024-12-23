from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    is_favorite: bool

class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    category: str
    is_favorite: bool

class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    is_favorite: bool

    class Config:
        orm_mode = True
