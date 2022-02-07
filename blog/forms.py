from django import forms
from .models import Comment, Post
from taggit.models import Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'drafted', 'tags']
        # wingets = {'tags': forms.TextInput(attrs={'class': 'form-control'})}
        