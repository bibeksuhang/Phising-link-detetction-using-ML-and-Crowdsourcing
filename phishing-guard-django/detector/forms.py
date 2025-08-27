from django import forms

class URLForm(forms.Form):
    url = forms.CharField(label='Enter a URL to check', max_length=300)
