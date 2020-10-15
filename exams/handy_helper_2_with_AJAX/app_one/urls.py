from django.urls import path
from . import views

urlpatterns = [
    ## RENDER
    path('', views.index),
    path('dashboard', views.dashboard),
    path('jobs/edit/<int:id>', views.jobsEdit),
    path('jobs/new', views.jobsNew),
    path('jobs_info/<int:id>', views.jobs_info),

    ## REDIRECT
        ## REGISTER/LOGIN/LOGOUT
    path('rd/reg', views.register),
    path('rd/login', views.login),
    path('rd/logout', views.logout),

        ##OTHER
    path('rd/new_job', views.new_job),
    path('rd/edit_job/<int:id>', views.edit_job),
    path('rd/remove_job/<int:id>', views.remove_job),
    path('rd/take_job/<int:id>', views.take_job),
    path('rd/give_up_job/<int:id>', views.give_up_job),

    ##AJAX
    path('rd/ajax/new_job', views.ajaxNew_job),
]