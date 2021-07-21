from django import forms


class CreateNewEntry(forms.Form):
    operation = forms.CharField(label="operation", max_length=200)
    store = forms.IntegerField(max_value=999)
    start_time = forms.DateTimeField(required=True, label="Presentation date", widget=forms.DateTimeInput) 
    end_time = forms.DateTimeInput()

class CreateNewWorksheet(forms.Form):
    # name = forms.CharField(max_length=99)
    date = forms.CharField(max_length=99)
    

    

    

    
