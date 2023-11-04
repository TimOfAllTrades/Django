
from django.shortcuts import render
from . import RSATools          #To import a file in the current directory, apparently a from . is necessary
# Create your views here.

#Use this to import requests?  I suppose....
from django.http import HttpResponse

# Create your tests here.



def home(request):
    
    
    InData = {
        'p': 19,
        'q': 48,
        'n': 65537
    }

    #Use render to return a home page with the path that is stored in /template of the current directory
    Has_q = request.GET.get('q', None)
    Has_p = request.GET.get('p', None)
    if Has_q is not None and Has_p is not None:
        InData['p'] = RSATools.nextprime(int(Has_p))
        InData['q'] = RSATools.nextprime(int(Has_q))
    
    print(InData)
    return render(request, 'main/about.html', InData)
    
    #return HttpResponse("Hello")