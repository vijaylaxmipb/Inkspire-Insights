from django.db import models
from django.contrib.auth.models import User
import datetime 
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(default="Default content goes here")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=True)
    dummy_field = models.CharField(max_length=10, null=True, blank=True) 
    featured_image = CloudinaryField('image', blank=True, null=True) 
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True) 
    

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_id': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.body} by {self.user.username}"

     
    def save(self, *args, **kwargs):
        if self.user and not self.name: 
            self.name = self.user.username
        super().save(*args, **kwargs)
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    blog_post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='events', null=True, blank=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title
    
    
