from django import forms
from .models import Entry

class CreateNewWorksheet(forms.Form):
    name = forms.CharField(max_length=30)
