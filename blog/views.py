from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Jeremy',
        'title' : 'Peterfield',
        'content' : 'Site information - picture mod to follow',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Peter',
        'title' : 'Bordon',
        'content' : 'Site information - picture mod to follow',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Simon',
        'title' : 'Farnborough',
        'content' : 'Site information - picture mod to follow',
        'date_posted': 'August 29, 2018'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
