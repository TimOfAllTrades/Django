from django.urls import path

#Importing the views page with the python code to handle the request
from . import views


urlpatterns = [
    path('', views.home, name='main-home'),     #The default home function
    #path('calculate/', views.calculate, name='main-calculate'),
    #path('encrypt/', views.encrypt, name='main-encrypt')
]
