from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductCreate(ProductBase): pass
class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    password: str

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
