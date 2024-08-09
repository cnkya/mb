from django.db import models


class Post(models.Model):  #inhearitance
    title= models.CharField(max_length=128) #lines 5-8:composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #timestamp (number of miliseconds since january 1st 1970 and django converts it to a readable form)

def __str__(self):
    return self.title
