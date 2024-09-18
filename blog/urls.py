# from . import views
# from django.urls import path

# urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.PostList.as_view(), name='blog_home'),  # Use the class-based view here
# ]

from django.urls import path
#from .views import PostList, home 
#from .views import post_detail
from . import views
from .views import EventsList
from .views import PostList, home, post_detail, event_detail



app_name = 'blog'

urlpatterns = [
    # Root URL for blog home
    path('', PostList.as_view(), name='blog_home'),  

    # Separate route for the home page
    path('home/', home, name='home'), 

    # Post detail view
    path('post/<int:post_id>/', post_detail, name='post_detail'),  

    # Events list view
    path('events/', EventsList.as_view(), name='events_list'),  
    
    # Event detail view
    path('event/<int:event_id>/', event_detail, name='event_detail'),
]