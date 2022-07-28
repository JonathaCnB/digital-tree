from apps.products.models import SubGroup
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Submit
from django import forms
from django.urls import reverse_lazy


class SubGroupCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-cad-sub-group"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("products:cad-sub-group"),
            "hx-target": "[name='sub_group']",
            "hx-swap": "outerHTML",
        }
        self.helper.layout = Layout(
            Column("name", css_class="form-group col-md-12"),
            Submit("submit", "Registrar"),
        )

    name = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Sub Grupo",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite o nome do sub grupo",
            }
        ),
    )

    class Meta:
        model = SubGroup
        fields = ("name",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        exists = SubGroup.objects.filter(
            name__iexact=name,
            company=self.company,
        ).exists()
        if exists:
            raise forms.ValidationError(
                "Sub Grupo já cadastrado",
                code="invalid",
            )
        return name

    def save(self, company, commit=True):
        sub_group = super().save(commit=False)
        sub_group.company = company
        if commit:
            sub_group.save()
        return sub_group
