from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Event  # Import models together
from .forms import CommentForm
from django.contrib import messages


class PostList(ListView):
    queryset = Post.objects.filter(status=1).exclude(title__exact='').exclude(content__exact='').exclude(excerpt__exact='')
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = 'post_list' 


class EventsList(ListView):
    model = Event
    template_name = 'blog/events_list.html'
    context_object_name = 'events'


def home(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'blog/home.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()


    return render(
    request,
    "blog/post_detail.html",
    {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )


    comment_form = CommentForm(data=request.POST)
    print("About to render template")

    events = Event.objects.all()  # Or filter for related events
    return render(request, 'blog/post_detail.html', {'post': post, 'events': events, "comments": comments,
        "comment_count": comment_count, "comment_form": comment_form,},)


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})  


def about(request):
    return render(request, 'about.html')  # Render the 'about.html' template
