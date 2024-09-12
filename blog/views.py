from django.shortcuts import render
from django.views import generic
from .models import Post
# from django.http import HttpResponse

# Create your views here.

#def blog_home(request):
    #return HttpResponse("Welcome to the Blog Home!")

# Create class based views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/blog_index.html"




