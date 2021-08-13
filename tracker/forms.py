from django import forms
from main.models import Entry
from django.utils.translation import ugettext_lazy as _


class UpdateEntry(forms.ModelForm):

    class Meta:
        model = Entry
        fields = [
            "start_time",
            "operation",
            "store",
            "end_time",
        ]
        widgets = {
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'id': 's',
                    'name': 's',
                    'step': '1',
                    'required': 'True',
                }
            ),
            'end_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'id': 'e',
                    'name': 'e',
                    'step': '1',
                    # 'required': 'True',
                }
            ),
        }
