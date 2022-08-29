from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
