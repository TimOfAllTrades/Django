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


def test(request):
    # context = {
    #    'Profile': Profiles
    # }
    # return HttpResponse('<h1>Blog Home</h1>')
    # Use requests http://192.168.1.116:8000/?q=hello&p=123
    print(request.GET.get('q', ''))
    print(request.GET.get('p', ''))
    return render(request, 'test/beep.html')
    # return render(request, 'blog/ContextVars.html', context)


def about(request):
    print("hello world")
    return render(request, 'blog/about.html')
    # return HttpResponse('<h1>Blog About</h1>')
