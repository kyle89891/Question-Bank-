from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['qus', 'subject']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text','is_correct']


# class registration(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['name','email','password']
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
#         }


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['email','password']
#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')
#         # Custom validation for email and password here if needed
#         return cleaned_data


class Signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','email']
        labels={'email':'Email'}