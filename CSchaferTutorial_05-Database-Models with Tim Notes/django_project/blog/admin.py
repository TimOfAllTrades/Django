from django.contrib import admin
from .models import Post        #To import the Post objects

admin.site.register(Post)       #This adds in the post functions to the admin interface.
