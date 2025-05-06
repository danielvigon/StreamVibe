from django import forms
from system.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'cpf', 'phone_number', 'email', 'address', 'image', 'register_date',]