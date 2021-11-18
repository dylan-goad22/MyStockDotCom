from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Investment, Stock

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InvestForm(ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'
        exclude = ['user', 'stock']

class CreateForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'