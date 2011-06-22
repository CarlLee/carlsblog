from posts.models import Post
from django.contrib import admin
from django.forms import Textarea
from django.db import models

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
               (None ,{'fields': ['title', 'published']}),
               (None ,{'fields': ['content']}),
    ]
    list_display = ('title', 'content', 'published')
    search_fields = ['title', 'content']
    date_hierarchy = 'published'
    change_form_template = 'change_form.html'
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={
                                                     'class':'xheditor {skin:\'nostyle\'}',
                                                     'style':'width: 100%; height: 450px',
                                                })},
    }
    
admin.site.register(Post, PostAdmin)