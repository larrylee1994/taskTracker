from django import forms


class CreateNewEntry(forms.Form):
    start_time = forms.DateTimeField(label="start_time")
    operation = forms.CharField(max_length=10)
    store = forms.IntegerField(label="store")
    end_time = forms.DateTimeField(label="end_time")


class CreateNewWorksheet(forms.Form):
    name = forms.CharField(max_length=30)
