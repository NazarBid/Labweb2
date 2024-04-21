from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Agent, Property, Client, Request ,CustomUser

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'specialty']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['type', 'address', 'price', 'agent']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'contact_email']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['client', 'property']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget = forms.Select(choices=CustomUser.ROLES)