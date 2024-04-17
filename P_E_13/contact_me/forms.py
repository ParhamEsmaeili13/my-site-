from django import forms
from .models import UserContact


class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = '__all__'

