from sqlalchemy.orm import Session
from . import models, schemas, auth

# Products
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Customers
def create_customer(db: Session, customer: schemas.CustomerCreate):
    hashed_pw = auth.hash_password(customer.password)
    db_customer = models.Customer(name=customer.name, email=customer.email, password=hashed_pw)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def authenticate_customer(db: Session, email: str, password: str):
    user = db.query(models.Customer).filter(models.Customer.email == email).first()
    if not user or not auth.verify_password(password, user.password):
        return False
    return user
