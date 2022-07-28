from apps.products.forms.cad_group import GroupCreateForm
from crispy_forms.utils import render_crispy_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View


class CadGroup(LoginRequiredMixin, View):
    template_name = "products/partials/form_cad_group.html"

    def get(self, *args, **kwargs):
        company = self.request.user.user_profiles.company
        ctx = {
            "form_group": GroupCreateForm(company=company),
        }
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        form = GroupCreateForm(self.request.POST)
        if form.is_valid():
            company = self.request.user.user_profiles.company
            form.save(company=company)
            name_group = form.cleaned_data["name"]
            html = f"""
                <input
                    type='text'
                    class='textInput
                    form-control'
                    name='group_select'
                    readonly
                    value={name_group}
                />
            """
            response = HttpResponse(html)
            response["HX-Target"] = "[name='group']"
            return response
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        response = HttpResponse(form_html)
        response["HX-Retarget"] = "#form-cad-group"
        return response
