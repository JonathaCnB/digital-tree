from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Div, Layout, Row, Submit
from django import forms
from django.urls import reverse_lazy

from apps.products.models import Product
from apps.stocks.models import Moviment


class MovimentCollectiveCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-mov-collective"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("stocks:collective"),
            "hx-target": "#form-collective",
            "hx-swap": "afterbegin",
        }
        self.helper.layout = Layout(
            HTML('<hr/>'),
            Row(
                Column("product", css_class="col-md-6"),
                Column("qty", css_class="col-md-3"),
                Div(
                    Submit(
                        "submit-login",
                        "Adicionar",
                        css_class="btn btn-block btn-primary"
                    ),
                    css_class='col-md-3 align-self-top'
                )
            ),
        )

        self.fields["product"].choices = [("", "Selecione um produto")] + list(
            self.fields["product"].choices
        )[1:]

    product = forms.ModelChoiceField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        queryset=Product.objects.filter(is_active=True),
        label=False,
        widget=forms.Select(
            attrs={
                "class": "form-control select2bs4",
                "required": "required",
            }
        ),
    )
    qty = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Informe a quantidade",
                "type": "number",
                "min": "1",
                "step": "1",
            }
        ),
    )
