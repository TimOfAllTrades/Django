from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm      #This is to import an existing form for user registration which handles password, username and email validity etc.  No need to recreate this from scratch
from django.contrib import messages     #To handle the success message when creating an account
from .forms import UserRegisterForm #The new creation form with email

# Create your views here.

def register(request):
    if request.method == 'POST':    #This is to check if the data was sent by button pressing.
        form = UserRegisterForm(request.POST)
        if form.is_valid():         #To check if form is valid, i.e. password is of correct strength
            form.save()     #Will save the form and automatically hash passwords etc
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')       #Redirect back to the home page when the account is successfully created is created
            

    else: #If it was not a post request just create a blank form
        form = UserRegisterForm()       #The existing user registration form
    return render(request, 'users/register.html', {'form' : form}) #Remember, only dictionaries can seemingly be passed through render's third argument
