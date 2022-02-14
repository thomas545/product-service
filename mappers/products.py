from core.response import error_response
from database.products_crud import ProductCRUD
from models.products import RetrieveProduct


def product_mapper(product: dict) -> dict:
    if product:
        return {
            "id": "%s" % product.get("_id", ""),
            "title": product.get("title", ""),
            "description": product.get("description", ""),
            "category_name": product.get("category_name", ""),
            "price": product.get("price", 0),
            "quantity": product.get("quantity", 0),
        }
    return {}


async def all_products(page_size=10, page_num=1):
    products = await ProductCRUD.all_products(page_num=page_num, page_size=page_size)
    products_list = []
    if products:
        async for product in products:
            products_list.append(product_mapper(product))
    return products_list


async def create_product(product: dict):
    product_obj = await ProductCRUD.add_product(product)
    return product_obj.inserted_id


async def get_single_product(pk: str):
    product = await reterive_product(pk)
    return product_mapper(product)


async def reterive_product(pk):
    get_product = await ProductCRUD.get_product({"id": pk})
    if not get_product:
        error_response("Product doesn't found!", 404)
    return get_product


async def update_product(pk: str, data: dict):
    await reterive_product(pk)
    update_product = await ProductCRUD.update_product(pk, data)
    if not update_product:
        error_response("Product doesn't updated!")
    return update_product


async def delete_product_with_pk(pk: str):
    await reterive_product(pk)
    await ProductCRUD.delete_product(pk)
