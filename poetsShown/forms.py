from django import forms

class PoetSearchForm(forms.Form):
    query = forms.CharField(label='Arama', max_length=100, 
    widget=forms.TextInput(attrs={'autocomplete': 'off'}))

class AuthorSearchForm(forms.Form):
    authorQuery = forms.CharField(label='Arama', max_length=40,
    widget=forms.TextInput(attrs={'autocomplete':'off'}))

class PopularitySearchForm(forms.Form):
    popularityQuery = forms.CharField(label='Arama', max_length=40,
    widget=forms.TextInput(attrs={'autocomplete':'off'}))