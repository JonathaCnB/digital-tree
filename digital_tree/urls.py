from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.users.urls")),
    path("", include("apps.portfolio.urls")),
    path("painel/", include("apps.core.urls")),
    path("messages/", include("apps.mensagens.urls")),
    path("produtos/", include("apps.products.urls")),
    path("movimentacao/", include("apps.stocks.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
