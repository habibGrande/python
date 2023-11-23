from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.root),
    path('process_money',views.process_money)

]