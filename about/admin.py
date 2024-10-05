from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin
from .models import CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    # Your configuration here
    summernote_fields = ('content',)
    

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'read',)
   

