from django.shortcuts import render
from .models import poetsShown
from .forms import PoetSearchForm

# Create your views here.
def index(request):
    if request.method == "GET":
        poets = poetsShown.objects.order_by('-id')
        form = PoetSearchForm()
        return render(request,'poetsShown/index.html',{
            'poets':poets,
            'form':form
            })
    else:
        form = PoetSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = poetsShown.objects.filter(poetName__icontains=query)
            return render(request, "poetsShown/search.html", {
                "poets": results,
                'searched': query
            }) 
            


def poetShow(request,author):
    poet = poetsShown.objects.filter(poetAuthor=author)
    return render(request,'poetsShown/poets.html',{
        'poet':poet
    })

"""
def search(request):
    if request.method == 'GET':
        form = PoetSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = poetsShown.objects.filter(poetName__icontains=query)
            return render(request, "poetsShown/search.html", {
                "results": results,
                'query': query
            }) 
    form = PoetSearchForm()
    poets = poetsShown.objects.all()
    return render(request, "poetsShown/search.html", {
        'form': form
    })
"""