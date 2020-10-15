from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('add_show', views.add_show),
    path('shows/<num>', views.shows_info),
    path('shows/<num>/edit', views.shows_edit),
    path('edit/show/<num>', views.edit_show),
    path('delete_show/<num>', views.delete_show),
]