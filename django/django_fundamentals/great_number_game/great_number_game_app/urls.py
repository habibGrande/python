from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.root),
    path('answer',views.answers)
    
]