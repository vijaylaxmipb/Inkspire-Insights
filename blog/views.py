from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView
from .models import Post, Event, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
    return render(request, 'blog/home.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
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
        else:
            messages.error(request, 'You must be logged in to comment!')
            return redirect('login')

    events = Event.objects.all()
    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'events': events, 
            'comments': comments,
            'comment_count': comment_count,
            'comment_form': comment_form
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


def comment_edit(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__id=post_id, user=request.user)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('blog:post_detail', post_id=post_id)
        else:
            messages.error(request, 'There was an error updating your comment.')
    else:
        comment_form = CommentForm(instance=comment)


    return render(request, 'blog/edit_comment.html', {
        'form': comment_form,
        'post_id': post_id,
    })


@login_required
def comment_delete(request, post_id, comment_id):
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)

    if request.method == "POST":
        comment.delete()  # Deletes the comment
        messages.success(request, 'Comment deleted successfully!')
        return redirect('blog:post_detail', post_id=post_id)

    return render(request, 'blog/confirm_delete.html', {'comment': comment, 'post': post})