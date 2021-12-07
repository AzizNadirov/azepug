from django import forms
from .models import Question, Answer, Comment



class QuestionCreateForm(forms.ModelForm):
     class Meta:
        model = Question
        fields = ['title', 'body', 'tags']


class AnswerCreateForm(forms.ModelForm):
     class Meta:
        model = Answer
        fields = ['body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'image']