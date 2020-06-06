from django import forms
from django.contrib.auth.models import User


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    comment = forms.CharField(required=False)