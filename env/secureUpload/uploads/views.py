from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [

    {
        'name': 'fileName',
        'extension' : '.txt',
        'date_posted': 'August 21, 2020',
    },
    {
        'name': 'file2',
        'extension' : '.doc',
        'date_posted': 'November 21, 2020',
    }
]


def home(request):
    context = {
        #'title': 'Home',
        'posts': posts
    }
    return render(request, 'uploads/home.html', context)


def upload(request):
    return render(request, 'uploads/upload.html')
    # {'title': 'Upload'}