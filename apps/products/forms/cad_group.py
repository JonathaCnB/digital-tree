from apps.products.models import Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Submit
from django import forms
from django.urls import reverse_lazy


class GroupCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.company = kwargs.pop("company", None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = "POST"
        self.helper.form_id = "form-cad-group"
        self.helper.attrs = {
            "autocomplete": "off",
            "hx-post": reverse_lazy("products:cad-group"),
            "hx-target": "select[name='group']",
            "hx-swap": "outerHTML",
        }
        self.helper.layout = Layout(
            Column("name", css_class="form-group col-md-12"),
            Submit("submit", "Registrar"),
        )

    name = forms.CharField(
        error_messages={"required": "Por favor digite um nome válido"},
        required=True,
        label="Grupo",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite o nome do grupo",
            }
        ),
    )

    class Meta:
        model = Group
        fields = ("name",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        exists = Group.objects.filter(
            name__iexact=name,
            company=self.company,
        ).exists()
        if exists:
            raise forms.ValidationError("Grupo já cadastrado", code="invalid")
        return name

    def save(self, company, commit=True):
        group = super().save(commit=False)
        group.company = company
        if commit:
            group.save()
        return group
