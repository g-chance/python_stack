from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses/destroy/<int:id>', views.courses_destroy_id),
    path('courses/comment/<int:id>', views.courses_comment_id),
    path('redirect/add_course', views.add_course),
    path('redirect/destroy_course/<int:id>', views.destroy_course),
    path('redirect/add_comment/<int:id>', views.add_comment),
    path('redirect/comments/destroy/<int:id>/<int:course>', views.destroy_comment)
]