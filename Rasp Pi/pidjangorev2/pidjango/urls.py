"""
URL configuration for pidjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#Be sure to import include from django urls
from django.urls import path, include

#If running a script directly include it here
#Input the python script that contains the "html constructor"
from pitestpage import views


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    #path('pitestpage', include('pitestpage.urls')),    #For additional URLs include file should be /[folder]/urls.py
    path('HelloWorld/', views.hello)

    #path('', include()),       #This is to be used for the default page
]
