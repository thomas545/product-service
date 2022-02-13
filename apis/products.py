from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from mappers.products import all_products, create_product
from core.response import response
from models.products import CreateProduct

products_router = APIRouter()


@products_router.get("/", description="products list")
async def get_all_products(page_num: int = 0, limit: int = 10):
    products_list = await all_products(page_num=page_num, page_size=limit)
    return response(products_list, "Product displayed successfully!")


@products_router.post("/add", description="products list")
async def add_product(product: CreateProduct):
    product_obj = jsonable_encoder(product)
    product_id = await create_product(product_obj)
    return response({"id": "%s" % product_id}, "Product Created!", status_code=201)

