from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#This python is necessary to create a new creation form object that has additional fields while inheriting all properties from the default userform class/object.

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']