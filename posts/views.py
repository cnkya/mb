from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post
#from django.urls import reverse this creates lookup url function


class PostListView(ListView):    #scan operation
    template_name = "posts/list.html"
    model = Post

class PostDetailView(DetailView):  #read single
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(CreateView):   #create new records
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    #success_url = reverse("list") use when you have an exception to the rule 

