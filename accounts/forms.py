from pyexpat import model
from django import forms

from accounts.models import User
from django.contrib.auth import authenticate
class SignupForm(forms.ModelForm):
    class Meta:
        model =User
        fields =['username','email','password']



class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password') 

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login credentials.")