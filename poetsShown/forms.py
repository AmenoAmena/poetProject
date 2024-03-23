from django import forms

class PoetSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, 
    widget=forms.TextInput(attrs={'autocomplete': 'off'}))
