"""
URL configuration for inkspire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from blog.views import home

from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'blog/404.html', status=404)


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path('blog/', blog_home, name='blog_home'),
    # path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    # path('home/', blog_views.home, name='home'),
    path("home/", include("blog.urls"), name="blog-urls"),
    path("", home, name="home"), 
 
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

handler404 = custom_404