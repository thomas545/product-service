from motor import motor_asyncio

MONGO_CONNECTION_URL = "mongodb+srv://<username>:<password>@<host>/<database_name>?retryWrites=true&w=majority"


CLIENT = motor_asyncio.AsyncIOMotorClient(MONGO_CONNECTION_URL)

database = CLIENT.ecommerce


products_collection = database.get_collection("products")





