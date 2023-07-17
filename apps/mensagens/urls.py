from django.urls import path

from apps.mensagens import views

app_name = "message"

urlpatterns = [
    path("send/", views.Send.as_view(), name="send"),
    path("webhook/", views.WebHook.as_view(), name="webhook"),
]
