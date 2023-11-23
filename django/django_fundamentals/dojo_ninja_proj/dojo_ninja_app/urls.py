from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.root),
    path('createDojo',views.createDojo),
    path('createNinja',views.createNinja)
    
]