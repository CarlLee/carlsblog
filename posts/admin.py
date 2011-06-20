from posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
               (None ,{'fields': ['title', 'published']}),
               (None ,{'fields': ['content']}),
    ]
    list_display = ('title', 'content', 'published')
    search_fields = ['title', 'content']
    date_hierarchy = 'published'
admin.site.register(Post, PostAdmin)