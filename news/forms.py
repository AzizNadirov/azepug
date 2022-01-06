from django import forms
from .models import Comment, News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'drafted', 'tags']
        # wingets = {}