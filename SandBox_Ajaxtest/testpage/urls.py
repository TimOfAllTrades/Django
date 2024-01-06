from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test-home'),
    #path('about/', views.about, name = 'blog-about'),
]
