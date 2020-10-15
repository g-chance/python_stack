from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('courses/destroy/<int:id>', views.courses_destroy_int),
    path('destroy_course/<int:id>', views.destroy_course),
]