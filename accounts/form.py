from dataclasses import field
from multiprocessing.connection import Client
from django import forms
from accounts.models import Clientt

class LoginForm(forms.ModelForm):
    class Meta:
        model = Clientt
        fields =['b_o_b','email','password',]


class SignupForm(forms.ModelForm):
    class Meta:
        model = Clientt
        fields =['email','username','password']