from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from employeapp.models import Employee,Company

from django.contrib.auth.forms import AuthenticationForm

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields="__all__"

class EmployeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})