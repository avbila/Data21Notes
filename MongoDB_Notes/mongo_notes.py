import pymongo
from pprint import pprint

client = pymongo.MongoClient()
# print(client)
db = client['starwars']
# print(db)

# same commands but snake case instead of camel case

# luke = db.characters.find_one({"name": "Luke Skywalker"})  # type dictionairy
# pprint(luke, sort_dicts=False)

# luke = db.characters.find({"name": "Luke Skywalker"})
# print(list(luke))
# for char in luke:
#     print(char["name"])

# blue = db.characters.find({"eye_color": "blue"})
# # for char in blue:
# #     print(char["name"])
# # or:
# blue_names = map(lambda x: x["name"], blue)
# pprint(list(blue_names))

# droids = db.characters.find({"species.name": "Droid"})
# droid_names = map(lambda x: x["name"], droids)
# pprint(list(droid_names))

# vader = db.characters.find_one({"name": {"$regex": "Vader"}},
#                                {"name": 1, "height": 1, "_id": 0})
# print(vader)

# yellow_eyes = db.characters.find({"eye_color": "yellow"},
#                                  {"name": 1, "_id": 0})
# pprint(list(yellow_eyes))

# male = db.characters.find({"gender": "male"},
#                           {"name": 1, "_id": 0}).limit(3)
# pprint(list(male))

# humans = db.characters.find(
#     {"$and": [
#         {"homeworld.name": "Alderaan"},
#         {"species.name": "Human"}
#     ]
#     },
#     {"name": 1, "_id": 0}
# )
# # or:
# humans = db.characters.find(
#     {"homeworld.name": "Alderaan",
#      "species.name": "Human"
#      },
#     {"name": 1, "_id": 0}
# )
# pprint(list(humans))

# female_height = db.characters.aggregate([
#     {"$match": {"gender": "female", "height": {"$ne": float("nan")}}},  # or use np.nan from numpy
#     {"$group": {"_id": "$gender", "avg_height": {"$avg" : "$height"}}}
# ])
# print(female_height.next())

# max_height = db.characters.aggregate([
#     {"$match": {"height": {"$ne": float("nan")}}},
#     {"$group": {"_id": None, "max_height": {"$max": "$height"}}}  # set group _id to None to group over everyone
# ]).next()["max_height"]
# char_tallest = db.characters.find(
#     {"height": max_height},
#     {"name": 1, "_id": 0}
# )
# pprint(list(char_tallest))
