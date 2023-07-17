import json

from crispy_forms.utils import render_crispy_form
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.generic import TemplateView, View

from apps.products.forms.product import ProductCreateForm, ProductUpdateForm
from apps.products.models import Product


class IndexProductView(LoginRequiredMixin, TemplateView):
    template_name = "products/index.html"
    extra_context = {"page_title": "Produtos"}


class ProductsList(LoginRequiredMixin, View):
    template_name = "products/partials/table_products.html"

    def get(self, *args, **kwargs):
        company = self.request.user.user_profiles.company
        qs_products = Product.objects.is_active(company=company)
        ctx = {"obj_list": qs_products}
        return render(self.request, self.template_name, ctx)


class CadProduct(LoginRequiredMixin, View):
    template_name = "products/partials/form_cad_product.html"
    template_list = "products/partials/table_products.html"

    def get(self, *args, **kwargs):
        user = self.request.user.user_profiles
        ctx = {
            "form": ProductCreateForm(user=user),
        }
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        user = self.request.user.user_profiles
        form = ProductCreateForm(self.request.POST, user=user)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=201,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "productsListChanged": None,
                            "showMessage": "Produto criado!!",
                        }
                    )
                },
            )
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        response = HttpResponse(form_html)
        response["HX-Retarget"] = "#form-product-cad"
        return response


class UpdateProduct(LoginRequiredMixin, View):
    template_name = "products/partials/form_cad_product.html"

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        instance = Product.objects.get(pk=pk)
        ctx = {
            "form": ProductUpdateForm(
                instance=instance,
                product_id=pk,
            ),
        }
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        pk = kwargs.get("pk")
        user = self.request.user.user_profiles
        instance = Product.objects.get(pk=pk)
        form = ProductUpdateForm(
            self.request.POST,
            instance=instance,
        )
        if form.is_valid():
            form.save(user=user)
            return HttpResponse(
                status=200,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "productsListChanged": None,
                            "showMessage": "Produto alterado!!",
                        }
                    )
                },
            )
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        response = HttpResponse(form_html)
        response["HX-Retarget"] = "#form-product-update"
        return response


class ExcudeProduct(LoginRequiredMixin, View):
    template_name = "products/partials/form_exclude_product.html"

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        product = Product.objects.get(pk=pk)
        ctx = {"object": product}
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        pk = kwargs.get("pk")
        product = Product.objects.get(pk=pk)
        product.is_active = False
        product.save()
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps(
                    {
                        "productsListChanged": None,
                        "showMessage": "Produto excluído!!",
                    }
                )
            },
        )


class SearchProducts(View):
    template_name = "products/partials/table_products.html"

    def post(self, *args, **kwargs):
        search = self.request.POST.get("table_search")
        company = self.request.user.user_profiles.company
        if search:
            qs_products = Product.objects.search(company=company, query=search)
        else:
            qs_products = Product.objects.is_active(company=company)
        ctx = {"obj_list": qs_products}
        return render(self.request, self.template_name, ctx)
