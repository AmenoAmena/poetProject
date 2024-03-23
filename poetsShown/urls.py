from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), 
    path("poet/<str:name>", views.poetShow, name='poet_show'),  
]
