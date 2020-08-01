from django.contrib import admin
from .models import Category, Post, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name_author', 'email', 'post', 'created', 'active')
#     list_filter = ['active', 'created','updated']
#     search_fields = ['name_author', 'email', 'body']