from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "login-user"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("users:login"),
        }
        self.helper.add_input(Submit("submit-login", "Logar"))

    username = forms.CharField(
        required=True,
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "placeholder": "Digite e-mail cadastrado",
                "id": "register-username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "id": "register-password",
            },
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        authenticated_user = authenticate(
            username=username,
            password=password,
        )
        if authenticated_user is None:
            raise ValidationError(
                {
                    "password": "E-mail ou senha inválido.",
                    "username": "E-mail ou senha inválido.",
                }
            )
