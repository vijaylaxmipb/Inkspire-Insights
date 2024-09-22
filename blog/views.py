from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Event  # Import models together


class PostList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


class EventsList(ListView):
    model = Event
    template_name = 'blog/events_list.html'
    context_object_name = 'events'


def home(request):
    return render(request, 'base.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    events = Event.objects.all()  # Or filter for related events
    return render(request, 'blog/post_detail.html', {'post': post, 'events': events, "comments": comments,
        "comment_count": comment_count,},)


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})  
