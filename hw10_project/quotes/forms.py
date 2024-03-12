from django.forms import ModelForm, CharField, TextInput
from .models import Author, Tag, Quote



class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True)
    born_date = CharField(max_length=50, required=True)
    born_location = CharField(max_length=150, required=True)
    description = TextInput()
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=1000, required=True)
    author = CharField(max_length=50, required=True)
    tags = CharField(max_length=100, required=True)
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']