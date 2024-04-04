from django.shortcuts import render
from .models import poets_shown,poet_author
from .forms import PoetSearchForm, AuthorSearchForm
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    if request.method == "GET":
        poets = poets_shown.objects.order_by('-id')
        form = PoetSearchForm()
        return render(request,'poetsShown/index.html',{
            'poets':poets,
            'form':form
            })
    else:
        form = PoetSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = poets_shown.objects.filter(poetName__icontains=query)
            return render(request, "poetsShown/search.html", {
                "poets": results,
                'searched': query
            }) 
            


def poetShow(request, pk):  
    poet = get_object_or_404(poets_shown, pk=pk) 
    poet.popularity += 1  
    poet.save() 
    author = poet.poetAuthor 
    authorPoet = poets_shown.objects.filter(poetAuthor=author)
    return render(request, 'poetsShown/poets.html', {
        'poet': poet,
        'author': author,
    })



def authorShow(request):
    if request.method == 'GET':
        authors = poet_author.objects.order_by('-id')
        authorForm = AuthorSearchForm()
        return render(request,'poetsShown/authors.html',{
            'authors':authors,
            'authorForm':authorForm
        })
    else:
        authorForm = AuthorSearchForm(request.POST)
        poets = poets_shown.objects.all()
        if authorForm.is_valid():
            authorQuery = authorForm.cleaned_data['authorQuery']
            results = poet_author.objects.filter(author__icontains=authorQuery)
            return render(request, 'poetsShown/authorSearch.html',{
                'authors':results,
                'searched':authorQuery,
                'poets':poets
            })

def authorPoets(request, pk):
    author = get_object_or_404(poet_author, pk=pk)
    authorPoet = poets_shown.objects.filter(poetAuthor=author).order_by('-id')
    return render(request, 'poetsShown/authorPoets.html', {
        'authorPoet': authorPoet,
        'author':author,
        })

def popularity(request):
    poets = poets_shown.objects.all()
    poets_ordered_popularity = poets.order_by('-popularity')
    return render(request, 'poetsShown/popularity.html',{
        'ordered_poets':poets_ordered_popularity
    })