from django import forms
from .models import Comment, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from taggit.models import Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']
        widgets = {'body': CKEditorUploadingWidget}


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'drafted', 'tags']
        widgets = {'tags': forms.TextInput(attrs={'class': 'form-control'}),
                         'content': CKEditorUploadingWidget()}
        