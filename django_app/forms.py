from django import forms
from django.contrib.auth.models import User


class user_reg(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class user_reg1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpass = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirmpass']
# superadmin
# admim(user model)


class user_login(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
