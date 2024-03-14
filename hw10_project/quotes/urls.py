
from django.urls import path
from .import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('page/<int:page>', views.main, name='root_paginate'),
    path('about/<str:author_id>', views.about_author, name='about'),
    path('tag/<str:tag>', views.show_tag, name='tag'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
]
