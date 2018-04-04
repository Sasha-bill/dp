
from django import forms


class UserForm(forms.Form):

    data = forms.CharField(max_length=100)

