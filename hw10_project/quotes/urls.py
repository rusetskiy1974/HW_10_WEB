
from django.urls import path
from .import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('about/<str:author_id>', views.about_author, name='about'),
    path('tag/<str:tag>', views.tag, name='tag'),
]
