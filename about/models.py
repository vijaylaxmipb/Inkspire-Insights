from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User  # Moved to the top
import datetime  # Import at the top, as per PEP 8

STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    title = models.CharField(max_length=300)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(default="Default content goes here")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="about_posts")
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):  # Fixed indentation
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)


class CollaborateRequest(models.Model):  # Fixed indentation
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

