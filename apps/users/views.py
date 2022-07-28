from crispy_forms.utils import render_crispy_form
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.generic import View

from apps.users.forms.login import LoginForm
from apps.users.forms.register import UserRegisterForm


class LoginView(View):
    template_name = "users/login.html"

    def get(self, *args, **kwargs):
        ctx = {"form": LoginForm()}
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        ctx = {}
        form = LoginForm(self.request.POST)
        if form.is_valid():
            try:
                authenticated_user = authenticate(
                    username=form.cleaned_data.get("username", ""),
                    password=form.cleaned_data.get("password", ""),
                )
                login(self.request, authenticated_user)
                response = render(self.request, "index.html")
                response["HX-Redirect"] = "/painel/"
                return response
            except Exception as e:
                print(e)
                form.add_error(
                    "username",
                    "algo deu errado, contacte o suporte",
                )
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)


class RegisterView(View):
    template_name = "users/register.html"

    def get(self, *args, **kwargs):
        ctx = {"form": UserRegisterForm()}
        return render(self.request, self.template_name, ctx)

    def post(self, *args, **kwargs):
        form = UserRegisterForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            response = render(self.request, "index.html")
            response["HX-Redirect"] = "/dashboard/"
            return response
        ctx = {}
        ctx.update(csrf(self.request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)
