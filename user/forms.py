from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        ),
    )

    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        ),
    )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-black px-3 py-2 rounded-md my-2 w-full",
            }
        ),
    )
