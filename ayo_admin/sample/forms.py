from django import forms
from accounts.models import Member
from django.contrib.auth import authenticate, login, logout

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, label="user name")
    password = forms.CharField(max_length=50, label="password")
    password_verify = forms.CharField(max_length=50, label="password confirmation")
    email = forms.EmailField(max_length=50, label="Email")
    dob = forms.DateField(input_formats=["%Y-%m-%d"], label="Date of Birthday")


    error_messages = {
        "mismatch" : "passwords don't match",
    }

    def clean_password2(self):
        password = self.cleaned_data["password"]
        password_verify = self.cleaned_data["password_verify"]
        if password_verify != password:
            raise forms.ValidationError(self.error_messages['mismatch'])
        return password_verify


class SigninForm(forms.Form):
    username = forms.CharField(max_length=50, label="user name")
    password = forms.CharField(max_length=50, label="password")


    def clean_password(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return password
        else:
            raise forms.ValidationError("Incorrect username or password")


class SettingsForm(forms.Form):
    username = forms.CharField(max_length=50, label="user name")
    email = forms.EmailField(max_length=50, label="Email")
    dob = forms.DateField(input_formats=["%Y-%m-%d"], label="Date of Birthday")
    country = forms.CharField(max_length=50, label="country", required=False)
    province = forms.CharField(max_length=50, label="province", required=False)
    city = forms.CharField(max_length=50, label="city", required=False)
    
