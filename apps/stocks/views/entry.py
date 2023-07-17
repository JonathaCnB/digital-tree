from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView

from apps.stocks.utils.moviment_register import moviment_register


class MovEntryView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/mov.html"
    extra_context = {
        "page_title": "Entrada",
        "url_mov": "/movimentacao/entrada/",
    }

    def post(self, *args, **kwargs):
        type_moviment = "e"
        if _ := moviment_register(self.request, type_moviment):
            return HttpResponse("Entrada Lançada")

        return HttpResponse("Operação não realizada")
