from django import forms

class QuizForm(forms.Form):
    country = forms.CharField(disabled=True, required=False,widget=forms.TextInput(attrs={'size':40}))
    country_hidden = forms.CharField()
    capital = forms.CharField(widget=forms.TextInput(attrs={'size':40}))