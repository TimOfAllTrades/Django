from django.shortcuts import render

# Create your views here.

#Use this to import requests?  I suppose....
from django.http import HttpResponse

# Create your tests here.

def hello(request):
    
    return HttpResponse("Hello")