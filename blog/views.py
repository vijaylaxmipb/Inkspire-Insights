from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3

def home(request):
    return render(request, 'home.html')
