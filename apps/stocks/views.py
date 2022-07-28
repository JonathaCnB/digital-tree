from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from apps.products.models import Product
from apps.stocks.forms.mov_single import MovimentCreateForm
from apps.stocks.models import Iten, Moviment


class IndexStocksView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/index.html"
    extra_context = {"page_title": "Movimentação"}


class MovExitView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/mov.html"
    extra_context = {
        "page_title": "Saída",
        "url_mov": "/movimentacao/saida/",
    }

    def post(self, *args, **kwargs):
        type_moviment = "s"
        moviment = _moviment_register(self.request, type_moviment)
        if moviment:
            return HttpResponse("Saída Lançada")

        return HttpResponse("Operação não realizada")


class MovEntryView(LoginRequiredMixin, TemplateView):
    template_name = "stocks/mov.html"
    extra_context = {
        "page_title": "Entrada",
        "url_mov": "/movimentacao/entrada/",
    }

    def post(self, *args, **kwargs):
        type_moviment = "e"
        moviment = _moviment_register(self.request, type_moviment)
        if moviment:
            return HttpResponse("Entrada Lançada")

        return HttpResponse("Operação não realizada")


def _moviment_register(request, type_moviment):
    profile = request.user.user_profiles
    product_pk = request.POST.get("product-pk", None)
    qty = request.POST.get("qty-informed", None)
    detail = request.POST.get("detail", None)
    if qty and product_pk:
        moviment = Moviment.objects.create(
            moviment=type_moviment,
            profile=profile,
        )
        product = Product.objects.get(pk=product_pk)
        if type_moviment == "e":
            new_stock = int(product.stock) + int(qty)
        else:
            new_stock = int(product.stock) - int(qty)

        product.stock = new_stock
        product.save()
        Iten.objects.create(
            moviment=moviment,
            product=product,
            qty=qty,
            stock=new_stock,
            detail=detail,
        )
        return True
    return False


class MovSingleView(LoginRequiredMixin, View):
    template_name = "stocks/partials/form_mov_single.html"

    def get(self, *args, **kwargs):
        ctx = {
            "form": MovimentCreateForm(),
        }
        return render(self.request, self.template_name, ctx)


class SearchProduct(View):
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


class MovimentList(View):
    template_name = "stocks/partials/table_moviment.html"

    def get(self, *args, **kwargs):
        location = self.request.GET.get("location")
        qs_moviment = Iten.objects.all()
        if location == "painel":
            qs_moviment = qs_moviment[0:10]
        ctx = {"obj_list": qs_moviment}
        return render(self.request, self.template_name, ctx)


class MovimentSearch(View):
    template_name = "stocks/partials/table_moviment.html"

    def get(self, *args, **kwargs):
        location = self.request.GET.get("location")
        search = self.request.GET.get("moviment_search")
        search_split = search.split(" ", 1)

        qs_moviment = Iten.objects.all()

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
            qs_moviment = qs_moviment[0:10]
        ctx = {"obj_list": qs_moviment}
        return render(self.request, self.template_name, ctx)
