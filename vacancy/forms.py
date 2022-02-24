from django import forms
from .models import Comment, Vacancy 



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class VacancyCreateForm(forms.ModelForm):
     class Meta:
        model = Vacancy
        fields = ['title', 'employer', 'content', 'contact', 'min_salary', 'dead_line', 'freelance', 'tags']
    

        widgets = {'dead_line': forms.DateInput(attrs= {'type': "date-local"})}
