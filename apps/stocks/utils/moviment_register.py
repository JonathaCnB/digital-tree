from apps.products.models import Product
from apps.stocks.models import Iten, Moviment


def moviment_register(request, type_moviment):
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
