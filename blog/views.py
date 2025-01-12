from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView
from .models import Post, Event, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Event
from .forms import EventForm
from django.utils.timezone import now

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
    events = Event.objects.filter(date__gte=now()).order_by('date')[:5]
    #return render(request, 'blog/home.html')
    return render(request, 'blog/home.html', {'events': events})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comments = post.comments.filter(approved=True).order_by("-created_at")
    comment_count = comments.count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post

            if request.user.is_authenticated:
                comment.approved = True

            comment.save()
            messages.success(request, 'Your comment has been posted successfully!')
            return redirect('blog:post_detail', post_id=post.id) 
        else:
            messages.error(request, 'Error submitting your comment.')

    # Fetch related posts (exclude the current post)
    posts = Post.objects.filter(status=1).exclude(id=post.id)[:3]

    events = Event.objects.all()
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'events': events, 
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form,
      
        }
    )


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})


def search_view(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})


def about(request):
    return render(request, 'about.html')

@login_required
def comment_edit(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__id=post_id, user=request.user)
    if request.method == "POST":
        form = CommentForm(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully.')
            return redirect('blog:post_detail', post_id=post_id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})


@login_required
def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__id=post_id, user=request.user)
    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('blog:post_detail', post_id=post_id)

    return render(request, 'blog/confirm_delete.html', {'comment': comment})

# blog/views.py
def learn_more(request):
    return render(request, 'blog/learn_more.html')

@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('blog:events_list')
    else:
        form = EventForm()

    return render(request, 'blog/create_event.html', {'form': form})