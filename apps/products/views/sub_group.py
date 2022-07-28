from apps.products.forms.cad_sub_group import SubGroupCreateForm
from crispy_forms.utils import render_crispy_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View


class CadSubGroup(LoginRequiredMixin, View):
    template_name = "products/partials/form_cad_sub_group.html"

    def get(self, *args, **kwargs):
        company = self.request.user.user_profiles.company
        ctx = {
            "form_sub_group": SubGroupCreateForm(company=company),
        }
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        form = SubGroupCreateForm(self.request.POST)
        if form.is_valid():
            company = self.request.user.user_profiles.company
            form.save(company=company)
            name_sub_group = form.cleaned_data["name"]
            html = f"""
                <input
                    type='text'
                    class='textInput
                    form-control'
                    name='sub_group_select'
                    readonly
                    value={name_sub_group}
                />
            """
            return HttpResponse(html)
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        response = HttpResponse(form_html)
        response["HX-Retarget"] = "#form-cad-sub-group"
        return response
