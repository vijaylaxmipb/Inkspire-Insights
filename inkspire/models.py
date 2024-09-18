from django.db import models

# Example of Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    status = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Example of Event model
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.name

