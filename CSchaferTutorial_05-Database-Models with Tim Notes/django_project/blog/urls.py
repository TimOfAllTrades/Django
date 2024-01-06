from django.urls import path
from . import views         #Need to import view objects and classes

urlpatterns = [
    path('', views.home, name='blog-home'),             #This is the URL pattern, name can be referenced in HTML variables
    path('about/', views.about, name='blog-about'),     
]
