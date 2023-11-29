from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.root),
    path('process',views.process),
    path('books/<int:id>',views.show),
    path('author',views.author),
    path('author/proccess',views.Author_process),
    path('author/<int:id>',views.author_show)


]
