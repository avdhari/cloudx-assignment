from django import forms
from contact.models import UserData


class NewContactForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ('name', 'email')

