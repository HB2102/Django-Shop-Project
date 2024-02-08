from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your First Name'})
    )

    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your Last Name'})
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your Email'})
    )

    username = forms.CharField(
        label='Username',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your Username'})
    )

    password1 = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder': 'Enter your Password'})
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'name': 'password',
                                          'type': 'password',
                                          'placeholder': 'Repeat your Password'})
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )
