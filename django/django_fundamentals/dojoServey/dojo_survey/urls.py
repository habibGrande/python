from django.urls import path , include 
from . import views

urlpatterns = [
    path('' ,views.root),
    path('result',views.show)
]