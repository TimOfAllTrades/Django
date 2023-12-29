from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm      #The user creation form, passwords username etc
from django.contrib import messages

# Create your views here.
def register(request):
    
    if request.method == 'POST':        #To check if password form is entered
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')  #This is the url pattern for the home page check blog/urls.py
    else:
        form = UserCreationForm()  #This is what creates all the extra password rules and text
    return render(request, 'users/register.html', {'form' : form})