import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.hw_10_web

with open('quotes.json', 'r', encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
       db.quotes.insert_one({
           'author': ObjectId(author['_id']),
           'tags': quote['tags'],
           'quote': quote['quote']


       })
