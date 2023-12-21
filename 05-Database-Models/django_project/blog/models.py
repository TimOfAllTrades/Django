from django.db import models
from django.utils import timezone               #Time zone
from django.contrib.auth.models import User

#Databases can be represented as classes.  These are called models
#Django has a built authentication system model.  These are imported in line 3


class Post(models.Model):
    #A post object inherits all the attributes (and presumably methods) of a model.Model object from the Django database
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
