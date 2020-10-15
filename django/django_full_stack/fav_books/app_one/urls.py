from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books_dash', views.books_dash),
    path('book_info/<int:id>', views.book_info),
    
    path('rd/reg', views.register),
    path('rd/add_book', views.add_book),
    path('rd/add_favorite/<int:id>', views.add_favorite),
    path('rd/login', views.login),
    path('rd/logout', views.logout),
    path('rd/edit_book/<int:id>', views.edit_book),
    path('rd/delete_book/<int:id>', views.delete_book),
]