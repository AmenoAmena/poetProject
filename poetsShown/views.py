from django.shortcuts import render
from .models import poetsShown

# Create your views here.
def index(request):
    poets = poetsShown.objects.all()
    return render(request,'poetsShown/index.html',{
        'poets':poets
        })

def poetShow(request,author):
    poet = poetsShown.objects.filter(poetAuthor=author)
    return render(request,'poetsShown/poets.html',{
        'poet':poet
    })
