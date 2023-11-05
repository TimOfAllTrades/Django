
from django.shortcuts import render
from . import RSATools          #To import a file in the current directory, apparently a from . is necessary
# Create your views here.

#Use this to import requests?  I suppose....
from django.http import HttpResponse
import json
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

def calculate(request):

    InData = {
        'p': 19,
        'q': 48,
        'n': 65537
    }
    print(request.POST)
    
    Has_q = int(request.POST.get('q', None))
    Has_p = int(request.POST.get('p', None))
    Has_n = int(request.POST.get('n', None))
    if Has_q is not None and Has_p is not None:
        InData['p'] = RSATools.nextprime((Has_p))
        InData['q'] = RSATools.nextprime((Has_q))
        
    
    if Has_n is not None:
        while RSATools.Eulers_GCD((InData['p']-1)*(InData['q']-1), (Has_n)) != 1:
            Has_n += 1
            Has_n = RSATools.nextprime((Has_n))
        InData['n'] = Has_n

    pkey = RSATools.Get_Private_Key(InData['p'], InData['q'],InData['n'])
    print(pkey)

    #resultcalc = HttpResponse("Hello")
    #print("StatusCode",resultcalc.status_code)
    print(InData)
    pqn = str(InData['p']) + "," + str(InData['q']) + "," + str(InData['n']) + "," + str(pkey)
    print("pqn",pqn)
    #print("httpresponsedata", HttpResponse("Hello"))
    payload =  {'success': True , 'ResponseText' : pqn}
    return HttpResponse(json.dumps(payload), content_type='application/json')