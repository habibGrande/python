from django.urls import path , include 
from . import views

urlpatterns = [ 
    path('shows',views.root),
    path('shows/new',views.new),
    path('create' ,views.create),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit',views.editPage),
    path('shows/<int:id>/update',views.edit),
    path('shows/<int:id>/destroy',views.delete)
    
]