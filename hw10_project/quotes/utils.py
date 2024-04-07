from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb://api_db:27017", username="root", password="example")
    db = client.hw_10_web
    return db


def get_top10_tags():
    all_tags = []
    db = get_mongodb()
    quotes = db.quotes.find()
    for quote in quotes:
        all_tags.extend(quote['tags'])

    tags_counts = {}
    for tag in all_tags:
        if tag in tags_counts:
            tags_counts[tag] += 1
        else:
            tags_counts[tag] = 1
    top10_tags = [tag[0] for tag in sorted(tags_counts.items(), key=lambda x: x[1], reverse=True)[:10]]
    return top10_tags
