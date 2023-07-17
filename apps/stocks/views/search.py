from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from apps.products.models import Product
from apps.stocks.models import Iten


class SearchProduct(LoginRequiredMixin, View):
    template_name = "stocks/partials/list_products_search.html"

    def get(self, *args, **kwargs):
        search = self.request.GET.get("product")
        company = self.request.user.user_profiles.company
        products = Product.objects.search(company=company, query=search)
        if search == "":
            return HttpResponse("")
        if not products:
            html = """
                <span
                    class="text-danger"
                >
                    Produto não encontrado
                </span>
            """
            return HttpResponse(html)
        ctx = {"obj_list": products}
        return render(self.request, self.template_name, ctx)


class MovimentSearch(View):
    template_name = "stocks/partials/table_moviment.html"

    def get(self, *args, **kwargs):
        location = self.request.GET.get("location")
        search = self.request.GET.get("moviment_search")
        search_split = search.split(" ", 1)
        company = self.request.user.user_profiles.company
        qs_moviment = Iten.objects.select_related("product")
        qs_moviment = qs_moviment.filter(product__company=company)

        if "+" not in search and "-" not in search:
            qs_moviment = qs_moviment.filter(
                product__product__icontains=search,
            )

        if search == "+":
            qs_moviment = qs_moviment.filter(moviment__moviment="e")

        if search == "-":
            qs_moviment = qs_moviment.filter(moviment__moviment="s")

        if len(search_split) > 1:
            if search_split[0] == "+":
                qs_moviment = qs_moviment.filter(moviment__moviment="e")
                qs_moviment = qs_moviment.filter(
                    product__product__icontains=search_split[1],
                )
            if search_split[0] == "-":
                qs_moviment = qs_moviment.filter(moviment__moviment="s")
                qs_moviment = qs_moviment.filter(
                    product__product__icontains=search_split[1],
                )

        if location == "painel":
            qs_moviment = qs_moviment[:10]
        ctx = {"obj_list": qs_moviment}
        return render(self.request, self.template_name, ctx)
