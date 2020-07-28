from django import forms
from .models import Comment_1

class Comment_1Form(forms.ModelForm):
    class Meta:
        model = Comment_1
        fields = ['name_author', 'email', 'body']