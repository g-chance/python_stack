from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success/<int:id>', views.success),
    path('rd/reg', views.register),
    path('rd/login', views.login),
    path('rd/logout', views.logout),
]