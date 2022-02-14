from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from mappers.products import (
    all_products,
    create_product,
    get_single_product,
    update_product,
    delete_product_with_pk,
)
from core.response import response
from models.products import CreateProduct, UpdateProduct

products_router = APIRouter()


@products_router.get("/", description="products list")
async def get_all_products(page_num: int = 1, limit: int = 10):
    products_list = await all_products(page_num=page_num, page_size=limit)
    return response(products_list, "Product displayed successfully!")


@products_router.post("/add", description="product create")
async def add_product(product: CreateProduct):
    product_obj = jsonable_encoder(product)
    product_id = await create_product(product_obj)
    return response({"id": "%s" % product_id}, "Product Created!", status_code=201)


@products_router.get("/{pk}", description="reterive product")
async def reterive_product(pk):
    product_obj = await get_single_product(pk)
    return response(product_obj, "Product Displayed!")


@products_router.put("/edit/{pk}")
async def edit_product(pk: str, edit_product: UpdateProduct):
    product_obj = jsonable_encoder(edit_product)
    await update_product(pk, product_obj)
    return response({"_id": pk}, "Product Updated!", status_code=200)


@products_router.delete("/delete/{pk}")
async def delete_product(pk: str):
    await delete_product_with_pk(pk)
    return response({"_id": pk}, "Product Deleted!", status_code=200)
