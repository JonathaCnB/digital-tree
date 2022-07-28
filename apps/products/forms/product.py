from apps.products.models import Group, Product, SubGroup
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse_lazy


class ProductCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-product-cad"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("products:cad-product"),
            "hx-target": "#cad-product-tbody",
            "hx-swap": "afterbegin",
        }
        self.helper.layout = Layout(
            Row(
                Column("product", css_class="form-group col-5"),
                FieldWithButtons(
                    "group",
                    StrictButton(
                        '<span class="fas fa-plus group"></span>',
                        css_class="group",
                        data_toggle="modal",
                        data_target="#modal-cad-group",
                        hx_get="/produtos/cad-group/",
                        hx_target="#modal-cad-group-content",
                        hx_swap="innetHTML",
                    ),
                    css_class="col-4",
                ),
                FieldWithButtons(
                    "sub_group",
                    StrictButton(
                        '<i class="fas fa-plus sub-group"></i>',
                        css_class="sub-group",
                        data_toggle="modal",
                        data_target="#modal-cad-sub-group",
                        hx_get="/produtos/cad-sub-group/",
                        hx_target="#modal-cad-sub-group-content",
                        hx_swap="innetHTML",
                    ),
                    css_class="col-3",
                ),
                css_class="form-row",
            ),
            Row(
                Column("barcode", css_class="form-group col-3"),
                Column("price", css_class="form-group col-3"),
                Column("unit", css_class="form-group col-2"),
                Column("minimum_stock", css_class="form-group auto"),
                css_class="form-row",
            ),
            Submit("submit", "Registrar"),
        )

    product = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Produto",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite o nome do produto",
            }
        ),
    )
    minimum_stock = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Estoque Minímo",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Quantidade miníma",
                "type": "number",
                "min": "0",
                "step": "1",
            }
        ),
    )
    barcode = forms.CharField(
        error_messages={"required": "Por favor digite um código válido"},
        required=False,
        label="Código de Barras",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Código de barras",
                "type": "text",
            }
        ),
    )
    price = forms.CharField(
        error_messages={"required": "Por favor digite um código válido"},
        required=False,
        label="Preço Unitário",
        widget=forms.TextInput(
            attrs={
                "placeholder": "R$ 0.00",
                "type": "number",
                "pattern": "[0-9]{4}.[0-9]{2}",
                "step": "0.01",
                "min": "0",
            }
        ),
    )
    group = forms.ModelChoiceField(
        label="Grupo",
        required=False,
        queryset=Group.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "required": "required",
            }
        ),
    )

    class Meta:
        model = Product
        fields = [
            "product",
            "minimum_stock",
            "unit",
            "barcode",
            "price",
            "sub_group",
            "group",
        ]

    def save(self, commit=True):
        product = super().save(commit=False)
        product.profile = self.user
        product.company = self.user.company
        if commit:
            product.save()
        return product

    def clean(self):
        cleaned_data = super(ProductCreateForm, self).clean()
        group_select = self.data.get("group_select")
        sub_group_select = self.data.get("sub_group_select")
        if group_select:
            group = Group.objects.get(name=group_select)
            self.cleaned_data["group"] = group
        if sub_group_select:
            sub_group = SubGroup.objects.get(name=sub_group_select)
            self.cleaned_data["sub_group"] = sub_group
        return cleaned_data


class ProductUpdateForm(ProductCreateForm):
    def __init__(self, *args, **kwargs):
        self.product_id = kwargs.pop("product_id", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-product-update"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy(
                "products:update-product",
                kwargs={"pk": self.product_id},
            ),
            "hx-target": "#cad-product-tbody",
            "hx-swap": "afterbegin",
        }
        self.helper.layout = Layout(
            Row(
                Column("product", css_class="form-group col-5"),
                FieldWithButtons(
                    "group",
                    StrictButton(
                        '<span class="fas fa-plus group"></span>',
                        css_class="group",
                        data_toggle="modal",
                        data_target="#modal-cad-group",
                        hx_get="/produtos/cad-group/",
                        hx_target="#modal-cad-group-content",
                        hx_swap="innetHTML",
                    ),
                    css_class="col-4",
                ),
                FieldWithButtons(
                    "sub_group",
                    StrictButton(
                        '<i class="fas fa-plus sub-group"></i>',
                        css_class="sub-group",
                        data_toggle="modal",
                        data_target="#modal-cad-sub-group",
                        hx_get="/produtos/cad-sub-group/",
                        hx_target="#modal-cad-sub-group-content",
                        hx_swap="innetHTML",
                    ),
                    css_class="col-3",
                ),
                css_class="form-row",
            ),
            Row(
                Column("barcode", css_class="form-group col-3"),
                Column("price", css_class="form-group col-3"),
                Column("unit", css_class="form-group col-2"),
                Column("minimum_stock", css_class="form-group auto"),
                css_class="form-row",
            ),
            Submit("submit", "Registrar"),
        )

    def save(self, user, commit=True):
        product = super().save(commit=False)
        product.profile = user
        product.company = user.company
        if commit:
            product.save()
        return product
