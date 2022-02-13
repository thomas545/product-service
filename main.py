from fastapi import FastAPI
from apis.products import products_router
app = FastAPI()

app.include_router(products_router, tags=["products"], prefix="/products")
