from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(max_length=50)
    widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 
                'placeholder': 'Input `#` for search for UPI'})}
    
