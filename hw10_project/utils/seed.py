import json

from mongoengine.errors import NotUniqueError

from models import Author, Quote


def main():
    with open('data/authors.json', encoding='utf-8') as fd:
        data_author = json.load(fd)
        for el in data_author:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except NotUniqueError:
                print(f"Автор вже існує {el.get('fullname')}")

    with open('data/quotes.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            for a in data_author:
                if a.get('fullname') == el.get('author'):
                    author, *_ = Author.objects(fullname=el.get('author'))
                    break

            quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
            quote.save()


if __name__ == '__main__':
    main()
