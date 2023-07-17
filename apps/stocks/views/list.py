from django.shortcuts import render
from django.views.generic import View

from apps.stocks.models import Iten


class MovimentList(View):
    template_name = "stocks/partials/table_moviment.html"

    def get(self, *args, **kwargs):
        location = self.request.GET.get("location")
        company = self.request.user.user_profiles.company
        qs_moviment = Iten.objects.select_related("product")
        qs_moviment = qs_moviment.filter(product__company=company)
        if location == "painel":
            qs_moviment = qs_moviment[:10]
        ctx = {"obj_list": qs_moviment}
        return render(self.request, self.template_name, ctx)
