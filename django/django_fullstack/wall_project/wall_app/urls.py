from django.urls import path , include 
from . import views

urlpatterns = [
    path('',views.root),
    path('register',views.create_user),
    path('wall',views.wall),
    path('postMessage',views.postMessage),
    path('login',views.login),
    path('destroy', views.logout),
    path('comment',views.comment),
    
    
]