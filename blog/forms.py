from django import forms
from .models import Comment

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class GuestCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'body']