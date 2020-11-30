from django.shortcuts import render
#from django.http import HttpResponse
from .models import File

def home(request):
    context = {
        'posts': File.objects.all()
    }
    return render(request, 'uploads/home.html', context)


def upload(request):
    return render(request, 'uploads/upload.html')
    # {'title': 'Upload'}