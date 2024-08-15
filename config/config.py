# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://pawanverma:999999999@fastapi.h1s5f.mongodb.net/"

# client = MongoClient(uri, server_api=ServerApi("1"))
# db = client.Blogging
# blogs_collection = db["blogs"]

# try:
#     client.admin.command('ping')
#     print("Connected to MongoDB")
# except Exception as e:
#     print(f"Failed to connect to MongoDB: {str(e)}")

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Connection URI
uri = "mongodb+srv://pawanverma:<password>@fastapi.h1s5f.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Access the database. Ensure consistent case (e.g., 'blogging' instead of 'Blogging').
db = client.blogging  # Make sure this name is consistent across your code

# Access the 'blogs' collection within the 'blogging' database
blogs_collection = db["blogs"]

# Ping the server to verify connection
try:
    client.admin.command('ping')
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")
