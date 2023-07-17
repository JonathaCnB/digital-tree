from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView

from apps.stocks.utils.moviment_register import moviment_register


class MovExitView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/mov.html"
    extra_context = {
        "page_title": "Saída",
        "url_mov": "/movimentacao/saida/",
    }

    def post(self, *args, **kwargs):
        type_moviment = "s"
        if _ := moviment_register(self.request, type_moviment):
            return HttpResponse("Saída Lançada")

        return HttpResponse("Operação não realizada")
