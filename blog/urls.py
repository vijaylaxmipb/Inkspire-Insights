from django.urls import path
from . import views
from .views import EventsList
from .views import PostList, home, post_detail, event_detail

app_name = 'blog'

urlpatterns = [
    # Root URL for blog home
    path('', PostList.as_view(), name='blog_home'),

    # Welcome page
    path('home/', views.home, name='home'),

    # Post detail view
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Events list view
    path('events/', EventsList.as_view(), name='events_list'),

    # Event detail view
    path('event/<int:event_id>/', event_detail, name='event_detail'),

    # About page
    path('about/', views.about, name='about'),

    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),

    # Search view
    path('search/', views.search_view, name='search'),

    # Comment edit and delete views
    path('post/<int:post_id>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('post/<int:post_id>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    ]