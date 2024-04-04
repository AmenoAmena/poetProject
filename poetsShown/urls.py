from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), 
    path("poet/<int:pk>", views.poetShow, name='poet_show'),
    path("author/",views.authorShow,name='author'), 
    path("authorpoet<int:pk>/", views.authorPoets, name='author_shown'),
    path("popularity/",views.popularity,name="popularity")
    
]

