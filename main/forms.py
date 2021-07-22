from django import forms
from django.utils import timezone


class CreateNewEntry(forms.Form):
    start_time = forms.DateTimeField(label="start_time")
    operation = forms.CharField(max_length=10)
    store = forms.IntegerField(label="store")
    end_time = forms.DateTimeField(label="end_time")


class CreateNewWorksheet(forms.Form):
    # name = forms.CharField(max_length=99)
    date = forms.CharField(max_length=99)
