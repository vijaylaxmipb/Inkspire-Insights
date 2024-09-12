# from . import views
# from django.urls import path

# urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.PostList.as_view(), name='blog_home'),  # Use the class-based view here
# ]

from django.urls import path
from .views import PostList, simple_view  # Directly import PostList

urlpatterns = [
    path('test/', simple_view, name='simple_view'),  # Test view
    path('', PostList.as_view(), name='blog_home'),  # Use PostList directly
]


