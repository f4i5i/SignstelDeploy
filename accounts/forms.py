from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','phone','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','phone','email']

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control form-control-alternative'}),
        }

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['cnic','dob','gender','city','area','postalCode','address','aboutMe','image']

        widgets = {
            'cnic' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'dob' : forms.DateInput(attrs={'class': 'form-control form-control-alternative', 'type':'date'}),
            'gender' : forms.Select(attrs={'class': 'form-control form-control-alternative'}),
            'city' : forms.Select(attrs={'class': 'form-control form-control-alternative'}),
            'area' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'address' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'postalCode' : forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'aboutMe' : forms.Textarea(attrs={'class': 'form-control form-control-alternative'}),
        }