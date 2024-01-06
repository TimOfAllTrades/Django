from django.apps import AppConfig

#This file is used to manage the template folder and access things inside


class BlogConfig(AppConfig):        #Blog config class must be registered in the settings.py file in the main django folder
    name = 'blog'                   #This references the subdirectory in the templates folder.
