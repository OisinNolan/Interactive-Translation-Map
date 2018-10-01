from django import forms

class getWord(forms.Form):
    word = forms.CharField(label='', initial='Enter a word', widget=forms.TextInput(attrs={'class' : 'forms'}))