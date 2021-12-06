from django.contrib import admin
from .models import Post, Comment, Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name_author', 'email', 'post', 'created', 'active')
#     list_filter = ['active', 'created','updated']
#     search_fields = ['name_author', 'email', 'body']