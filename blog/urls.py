# from . import views
# from django.urls import path

# urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.PostList.as_view(), name='blog_home'),  # Use the class-based view here
# ]

from django.urls import path
from .views import PostList  # Only import PostList

urlpatterns = [
    path('', PostList.as_view(), name='blog_home'),  # Use PostList directly
]

