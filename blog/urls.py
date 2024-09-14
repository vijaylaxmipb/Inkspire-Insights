# from . import views
# from django.urls import path

# urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.PostList.as_view(), name='blog_home'),  # Use the class-based view here
# ]

from django.urls import path
from .views import PostList, home  # Only import 


app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='blog_home'),  
    path('home/', home, name='home'), 
]