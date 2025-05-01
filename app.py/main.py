from fastapi import FastAPI
from .routers import products, customers, users
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(users.router, tags=["Auth"])

