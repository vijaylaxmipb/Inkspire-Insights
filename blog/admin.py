from django.contrib import admin
from .models import Post, Comment, Event
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('status','created_at',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    
# Register your models here.
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'body', 'created_at', 'approved', 'active')
    list_filter = ('approved', 'active')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'blog_post')
    search_fields = ('title', 'description', 'blog_post__title')
    list_filter = ('date',)