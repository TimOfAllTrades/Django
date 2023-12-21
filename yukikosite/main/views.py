from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def home(request):

    InData = {
        'p':19,
        'q':17,
    }

    return render(request, 'main/index.html', InData)
