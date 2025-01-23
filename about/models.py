from django.db import models
from django.contrib.auth.models import User
import datetime

STATUS = ((0, "Draft"), (1, "Published"))


class About(models.Model):
    title = models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to='about_images/',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.profile_image:
            return self.profile_image.url
        return '/static/images/default-placeholder.jpeg'


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
