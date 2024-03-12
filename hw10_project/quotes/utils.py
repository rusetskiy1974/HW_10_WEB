from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://localhost:27017", username="root", password="example")
    db = client.hw_10_web
    return db
