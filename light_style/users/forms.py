from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from users.models import User


class RegistrationForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'telephone',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
        help_texts = {
            'username': "Letters and digits only"
        }

    def save(self, commit=True):
        self.instance.password = make_password(self.cleaned_data['password'])
        return super().save(self)

    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return self.cleaned_data

    def clean_username(self):
        username = self.data['username']
        if not username.isalpha():
            raise forms.ValidationError("Username contains forbidden characters")

        return username

    def clean_telephone(self):
        telephone = self.data['telephone']
        if not telephone.isdigit():
            raise forms.ValidationError("Telephone should  contain ONLY digits")

        return telephone


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def get_user(self, request):
        return authenticate(
            request,
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

