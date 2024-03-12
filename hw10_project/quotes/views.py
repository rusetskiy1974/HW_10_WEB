from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from bson import ObjectId

from django.contrib.auth.decorators import login_required
from .models import Author, Quote, Tag

from .utils import get_mongodb


def tag(request, tag):
    db = get_mongodb()
    quotes = db.quotes.find()

    for quote in quotes:
        if tag in quote['tags']:
            return render(request, 'quotes/tag.html', context={"quote": quote, "tag": tag})


def about_author(request, author_id):
    db = get_mongodb()
    author = db.authors.find_one({"_id": ObjectId(author_id)})
    # author = get_object_or_404(Author, pk=str(author_id))
    # print(author)

    return render(request, 'quotes/about.html', context={"author": author})


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_on_page})
