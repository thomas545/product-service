from database.products_crud import ProductCRUD
from models.products import RetrieveProduct


def product_mapper(product: dict) -> dict:
    return {
        "id": "%s"% product.get("_id", ""),
        "title": product.get("title", ""),
        "description": product.get("description", ""),
        "category_name": product.get("category_name", ""),
        "price": product.get("price", 0),
        "quantity": product.get("quantity", 0),
    }


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
