from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    body = models.TextField(default='Default body text')  # Added default value
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
)

content = models.TextField()
created_on = models.DateTimeField(auto_now_add=True)
status = models.IntegerField(choices=STATUS, default=0)
excerpt = models.TextField(blank=True)
updated_on = models.DateTimeField(auto_now=True)


class Meta:
        ordering = ["-created_on"]

def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)  
    approved = models.BooleanField(default=False)


class Meta:
        ordering = ["created_on"]

def __str__(self):
        return f"Comment {self.body} by {self.author}"
    


