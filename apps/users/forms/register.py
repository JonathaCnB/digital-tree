from apps.users.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from utils.forms import strong_password


class UserRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "register-user"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("users:register"),
        }
        self.helper.add_input(Submit("submit", "Registrar"))

    first_name = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu nome aqui",
            }
        ),
    )
    last_name = forms.CharField(
        error_messages={"required": "Por favor digite um sobrenome válido"},
        required=True,
        label="Sobrenome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu sobrenome aqui",
            }
        ),
    )
    email = forms.CharField(
        error_messages={"required": "Por favor digite um e-mail válido"},
        required=True,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "placeholder": "Digite seu melhor e-mail",
            }
        ),
        # help_text="Digite seu melhor e-mail",
        label="E-mail",
    )
    password = forms.CharField(
        error_messages={
            "required": "Por favor digite uma senha válida",
            "min_length": "Senha não pode conter menos que 8 caracteres",
        },
        required=True,
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite uma senha forte",
            },
        ),
        help_text=(
            "Deve conter no mínimo 8 digitos, letas maiúsculas e números"
        ),  # noqa
        validators=[strong_password],
        min_length=8,
    )
    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repita sua senha",
            },
        ),
        error_messages={"required": "É necessário confirmar a senha"},
        label="Confirmação de senha",
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirm",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError("E-mail já em uso", code="invalid")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise ValidationError(
                {
                    "password": "Campos de senha não são identicos",
                }
            )
