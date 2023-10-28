from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html')


def about(request):
    print("hello world")
    return HttpResponse('<h1>Blog About</h1>')
