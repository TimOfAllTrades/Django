
from django.shortcuts import render
from . import RSATools          #To import a file in the current directory, apparently a from . is necessary
# Create your views here.

#Use this to import requests?  I suppose....
from django.http import HttpResponse

# Create your tests here.



def home(request):
    print("hello")
    InData = {
        'p': 19,
        'q': 48,
        'n': 65537
    }
    #Use render to return a home page with the path that is stored in /template of the current directory
    print(request.GET.get('q', ''))
    print(request.GET.get('p', ''))
    
    InData['p'] = RSATools.nextprime(int(request.GET.get('p', '10')))
    print(InData)
    return render(request, 'main/about.html', InData)
    
    #return HttpResponse("Hello")