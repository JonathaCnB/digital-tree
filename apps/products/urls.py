from django.urls import path

from apps.products.views import group, product, sub_group

app_name = "products"

urlpatterns = [
    path("", product.IndexProductView.as_view(), name="index"),
    path("cad-group/", group.CadGroup.as_view(), name="cad-group"),
    path("cad-product/", product.CadProduct.as_view(), name="cad-product"),
    path(
        "cad-product/<int:pk>/update/",
        product.UpdateProduct.as_view(),
        name="update-product",
    ),
    path(
        "cad-sub-group/",
        sub_group.CadSubGroup.as_view(),
        name="cad-sub-group",
    ),
    path(
        "product/<int:pk>/exclude/",
        product.ExcudeProduct.as_view(),
        name="exclude",
    ),
    path("search/", product.SearchProducts.as_view(), name="search"),
]

urlpatterns += [
    path(
        "hx-get-produts/",
        product.ProductsList.as_view(),
        name="hx-get-products",
    ),
]
