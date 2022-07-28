from apps.stocks.models import Moviment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Div, Field, Layout, Row
from django import forms


class MovimentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-mov-single"
        self.helper.attrs = {
            "autocomplete": "off",
        }
        self.helper.layout = Layout(
            Row(
                Column("moviment", css_class="col-md-2"),
                Column(
                    Field(
                        "product",
                        hx_get="/movimentacao/search-product/",
                        hx_trigger="keyup",
                        hx_target="#feedback-search",
                        hx_swap="innerHTML",
                        required="required",
                    ),
                ),
            ),
            Row(
                Div(id="feedback-search", css_class="col-md-12"),
            ),
        )

    product = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Produto",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome ou Código de barras",
            }
        ),
    )
    qty = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Quantidade",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Quantidade",
                "type": "number",
                "min": "0",
                "step": "1",
            }
        ),
    )

    class Meta:
        model = Moviment
        exclude = ("profile", "is_active")
