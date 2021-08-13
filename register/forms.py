from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label=_("First Name"))
    last_name = forms.CharField(max_length=20, label=_("Last Name"))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
