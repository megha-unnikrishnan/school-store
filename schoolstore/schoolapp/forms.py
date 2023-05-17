# authentication/forms.py
from django import forms
from .models import Registration


class LoginForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password', 'cpassword']


class AdmissionForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = formPage
    #     fields = ['name', 'dob', 'age', 'gender', 'mob', 'email', 'address', 'department', 'courses', 'purposes',
    #               'materials']
