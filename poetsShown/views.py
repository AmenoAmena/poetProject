from django.shortcuts import render
from .models import poets_shown,poet_author
from .forms import PoetSearchForm

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
            


def poetShow(request,name):
    poet = poets_shown.objects.filter(poetName=name)
    return render(request,'poetsShown/poets.html',{
        'poet':poet
    })

def authorShow(request):
    authors = poet_author.objects.all()
    poets_shown_list = poets_shown.objects.all()
    return render(request,'poetsShown/authors.html',{
        'authors':authors,
        'poets_shown':poets_shown_list
    })

def authorPoets(request,author):

    author = poet_author.objects.get(author=author)

    authorPoet = poets_shown.objects.filter(poetAuthor=author)

    return render(request,'poetsShown/authorPoets.html',{
        'authorPoet':authorPoet,
    })