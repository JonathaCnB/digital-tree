from django.urls import path

from apps.portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("portifolio/", views.Index.as_view(), name="index"),
]
