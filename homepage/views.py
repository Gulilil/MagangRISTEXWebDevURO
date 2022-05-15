from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Hello World!</h1>")
    return render(request, 'home.html', {})

def tema1(request, *args, **kwargs):
    return render(request, 'tema1.html', {})

def tema7(request, *args, **kwargs):
    return render(request, 'tema7.html', {})

def tema8(request, *args, **kwargs):
    return render(request, 'tema8.html', {})

def tema12(request, *args, **kwargs):
    return render(request, 'tema12.html', {})