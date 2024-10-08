from django.shortcuts import render
from .models import poets_shown,poet_author
from .forms import PoetSearchForm, AuthorSearchForm, PopularitySearchForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    poets = poets_shown.objects.order_by('-id')

    paginator = Paginator(poets, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == "GET":
        form = PoetSearchForm()
    else:
        form = PoetSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = poets_shown.objects.filter(poetName__icontains=query)
            return render(request, "poetsShown/search.html", {
                "results": results,  
                'searched': query,
                'form': form  
            }) 

    return render(request,'poetsShown/index.html',{
        'page_obj': page_obj,  
        'form': form
    })
            

def poetShow(request, name):  
    poet = get_object_or_404(poets_shown, poetName=name) 
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

def authorPoets(request, poetAuthor):
    author = get_object_or_404(poet_author, author=poetAuthor)
    authorPoet = poets_shown.objects.filter(poetAuthor=author).order_by('-id')
    return render(request, 'poetsShown/authorPoets.html', {
        'authorPoet': authorPoet,
        'author':author,
        })

def popularity(request):
    if request.method == 'GET':
        form = PopularitySearchForm()
        poets = poets_shown.objects.all()
        poets_ordered_popularity = poets.order_by('-popularity')
        return render(request, 'poetsShown/popularity.html',{
            'ordered_poets':poets_ordered_popularity,
            'form':form
        })
    else:
        form = PopularitySearchForm(request.POST)
        if form.is_valid():
            popularityQuery = form.cleaned_data['popularityQuery']
            results = poets_shown.objects.filter(poetName__icontains=popularityQuery)
            return render(request, "poetsShown/popularitySearch.html", {
                "poets": results,
                'searched': popularityQuery
            })  



