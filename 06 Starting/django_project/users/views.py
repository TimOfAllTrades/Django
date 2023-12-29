from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    form = UserCreationForm()  #This is what creates all the extra password rules and text
    return render(request, 'users/register.html', {'form' : form})