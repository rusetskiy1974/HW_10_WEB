import os

from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE
from dotenv import load_dotenv

load_dotenv()
db_uri = os.environ.get("DB_LOCAL_URI")
connect(db='hw_10_web', host=db_uri)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=100))
    quote = StringField()
    meta = {"collection": "quotes"}
