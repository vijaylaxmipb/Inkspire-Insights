from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Event 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

class EventsList(generic.ListView):
    model = Event
    template_name = 'blog/events_list.html'
    context_object_name = 'events'

def home(request):
    return render(request, 'inkspire/home.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    events = Event.objects.all()  
    return render(request, 'blog/post_details.html', {'post': post, 'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})
