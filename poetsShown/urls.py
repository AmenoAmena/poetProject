from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'), 
    path("poet/<str:name>", views.poetShow, name='poet_show'),
    path("author/",views.authorShow,name='author'), 
    path("authorpoet/<str:poetAuthor>/", views.authorPoets, name='author_shown'),
    path("popularity/",views.popularity,name="popularity")
    
]

