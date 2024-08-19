from django import forms
from .models import UrlDb

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlDb
        fields = ['url','short_url']