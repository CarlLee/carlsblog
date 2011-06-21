from django import forms

class PostForm(forms.Form):
    title = forms.CharField(50, 3)
    content = forms.CharField()
    