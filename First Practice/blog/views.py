from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

Profiles = [
    {
        'Name': 'Tim',
        'Age': '39',
        'Education': 'PhD.'
    },
    {
        'Name': 'Josh',
        'Age': '36',
        'Education': 'MS.'
    }

]


def home(request):
    context = {
        'Profile': Profiles
    }
    
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/ContextVarsChild.html', context)
    # return render(request, 'blog/ContextVars.html', context)


def about(request):
    print("hello world")
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1>Blog About</h1>')
