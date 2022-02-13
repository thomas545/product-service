from .connection import products_collection


class ProductsReposatory:
    # def product_obj_mapper(self, obj):
    #     object_mapped = {}

    #     for k, v in obj.items():
    #         object_mapped[k] = v
    #     return object_mapped

    async def all_products(self, page_size=10, page_num=1):
        skips = page_size * (page_num -1)
        return products_collection.find().skip(skips).limit(page_size)

    async def add_product(self, product: dict):
        product_obj = await products_collection.insert_one(product)
        return product_obj

    async def get_product(self, fields: dict):
        fields = await self.validate_get_fields(fields=fields)
        student = await products_collection.find_one(**fields)
        return student

    def validate_get_fields(self, fields: dict):
        keys = list(fields.keys())
        if "id" in keys and "_id" not in keys:
            id_value = fields.get("id", "")
            fields["_id"] = id_value
            fields.pop("id")
        return fields


ProductCRUD = ProductsReposatory()
