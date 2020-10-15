from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('rd/reg', views.register),
    path('rd/login', views.login),
]