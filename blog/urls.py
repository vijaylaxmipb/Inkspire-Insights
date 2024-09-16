# from . import views
# from django.urls import path

# urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),
    # path('', views.PostList.as_view(), name='blog_home'),  # Use the class-based view here
# ]

from django.urls import path
from .views import PostList, home  # Only import 
from . import views



app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='blog_home'),  
    #path('', PostList.as_view(), name='home'),
    path('home/', home, name='home'), 
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.EventsList.as_view(), name='home'),
    path("<int:event_id>/", views.event_detail, name="event_detail")
    
]
 