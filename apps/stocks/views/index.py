from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexStocksView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/index.html"
    extra_context = {"page_title": "Movimentação"}
