from django.urls import path
from . import views
from .views import EventsList
from blog.views import PostList, home, post_detail, event_detail, EventsList, learn_more


app_name = 'blog'

urlpatterns = [
    
    path('', PostList.as_view(), name='blog_home'),
    path('home/', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('events/', EventsList.as_view(), name='events_list'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('search/', views.search_view, name='search'),
    path('learn-more/', views.learn_more, name='learn_more'),
    
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('post/<int:post_id>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/', views.EventsList.as_view(), name='events_list'), 
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('', PostList.as_view(), name='blog_home'),

    
    

    ]