from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<num>', views.books),
    path('add_author/<num>', views.add_author_to_book),
    path('author', views.author),
    path('add_author', views.add_author),
    path('author_info/<num>', views.author_info),
    path('add_book/<num>', views.add_book_to_author),
    path('home', views.home),
]