from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from apps.stocks.forms.mov_collective import MovimentCollectiveCreateForm
from apps.stocks.forms.mov_single import MovimentCreateForm
from apps.stocks.utils.moviment_register import moviment_register


class MovCollectiveView(LoginRequiredMixin, View):
    template_name = "stocks/collective.html"
    extra_context = {

        "url_mov": "/movimentacao/entrada/",
    }

    def get(self, *args, **kwargs):
        ctx = {
            "form_single": MovimentCreateForm(),
            "form": MovimentCollectiveCreateForm(),
            "page_title": "Multipla",
        }
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        type_moviment = "e"
        form = MovimentCollectiveCreateForm(self.request.POST)
        form_single = MovimentCreateForm(self.request.POST)
        print(form, form_single, sep='\n')
        # if _ := moviment_register(self.request, type_moviment):
        #     return HttpResponse("Entrada Lançada")

        return HttpResponse("Operação não realizada")


class NewProductCollective(LoginRequiredMixin, View):
    template_name = "stocks/partials/form_collective.html"

    def get(self, *args, **kwargs):
        ctx = {
            "form": MovimentCollectiveCreateForm(),
        }
        return render(self.request, self.template_name, ctx)
