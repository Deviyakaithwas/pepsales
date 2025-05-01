from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Product)
def create(product: schemas.ProductCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.Product])
def read(skip: int = 0, limit: int = 10, db: Session = Depends(database.SessionLocal)):
    return crud.get_products(db, skip, limit)
