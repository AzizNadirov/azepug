from django import forms
from .models import Comment, News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'drafted', 'tags']
        # wingets = {}