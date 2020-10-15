from django.urls import path
from . import views

urlpatterns = [
    ## RENDER
    path('', views.index),
    path('books', views.books),
    path('books/add', views.booksAdd),
    path('book_info/<int:id>', views.book_info),
    path('user_info/<int:id>', views.user_info),


    ## REDIRECT
    path('rd/reg', views.register),
    path('rd/login', views.login),
    path('rd/logout', views.logout),

    path('rd/add_book', views.add_book),
    path('rd/add_review/<int:id>', views.add_review),
    path('rd/del_review/<int:id>', views.del_review),
]