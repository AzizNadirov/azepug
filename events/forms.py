from django import forms
from .models import Event, Comment



class EventCreateForm(forms.ModelForm):
     class Meta:
        model = Event
        fields = ['title', 'organiser', 'content', 'starts_at', 'ends_at', 'tags']
        widgets = {'starts_at': forms.DateTimeInput(attrs= {'type': "datetime-local"}), 
            'ends_at': forms.DateTimeInput(attrs= {'type': 'datetime-local'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']