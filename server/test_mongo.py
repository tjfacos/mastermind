import pymongo
# from modules.network.connection_uri import connection_uri as CONNECTION
from connection_uri import connection_uri as CONNECTION

client = pymongo.MongoClient(CONNECTION)
db = client["mastermindDB"]
users_collection = db["users"]

users_collection.insert_one({
    "username": "tom",
    "password": "password123"
})

# print(client.list_database_names())
# print(db.list_collection_names())

