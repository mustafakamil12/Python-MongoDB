import pymongo

# Connect to MongoDB container
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")


# Access database if exist if not it will create one.
db = client["movies"]

# Access collection
collection = db["movie"]

# return all collections in the db above
collList = []
try:
    collList = db.list_collection_names()
    print(f"Hello I find this collecion/s: {collList}")
except:
    print("noting found ...")

# check if a specific collections exist 
if collList:
    if 'actors' in collList:
        print("The collection is exists.")

# Insert data
data = {"name" : "Iron Man 2"}
collection.insert_one(data)

# Insert data
data = {"name" : "Iron Man 1"}
collection.insert_one(data)

# Query data
results = collection.find({"name": "Iron Man 2"})
for result in results:
    print(result)

# delete document
myquery = {"name":"Iron Man 1"}
mycol = db['movie']
mycol.delete_one(myquery)