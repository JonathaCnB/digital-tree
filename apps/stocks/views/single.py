from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View

from apps.stocks.forms.mov_single import MovimentCreateForm


class MovSingleView(LoginRequiredMixin, View):
    template_name = "stocks/partials/form_mov_single.html"

    def get(self, *args, **kwargs):
        ctx = {
            "form": MovimentCreateForm(),
        }
        return render(self.request, self.template_name, ctx)
