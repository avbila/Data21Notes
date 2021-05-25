import pymongo
from pprint import pprint

# Need to put in the same url as in compass db.
client = pymongo.MongoClient("mongodb://3.125.46.51:27017")
db = client['demo']

# print(client.list_database_names())
# print(db.list_collection_names())

x = db.hello.find()
pprint(list(x), sort_dicts=False)

db.hello.insert_one({"cat": "bob", "mouse": 45})
db.hello.insert_one({"Dog": "bingo", "mouse": 4.5})
db.hello.insert_one({"Rabbit": "clint", "mouse": "No way"})
