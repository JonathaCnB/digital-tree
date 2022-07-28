from django.urls import path

from apps.stocks import views

app_name = "stocks"

urlpatterns = [
    path("", views.IndexStocksView.as_view(), name="index"),
    path("saida/", views.MovExitView.as_view(), name="exit"),
    path("entrada/", views.MovEntryView.as_view(), name="entry"),
    path("mov-single/", views.MovSingleView.as_view(), name="mov-single"),
    path("search-product/", views.SearchProduct.as_view(), name="search"),
    path("moviment/", views.MovimentList.as_view(), name="moviment"),
    path("moviment-search/", views.MovimentSearch.as_view(), name="moviment-search"),
]
