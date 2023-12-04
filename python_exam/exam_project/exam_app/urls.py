from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('destroy', views.logout),
    path('login', views.login),
    path('new',views.report_page),
    path('Report',views.createReport),
    path('edits',views.editPage),
    path('edit',views.edit),
    path('delete',views.delete),
    path('show',views.show)
   
    

]