from django.db import models

from apps.common.models import TimeStampedUUIDModel
from apps.products.models import Product
from apps.users.models import Profile


class MovimentStatus(models.TextChoices):
    INPUT = "e", "Entrada"
    OUTPUT = "s", "Saida"


class Moviment(TimeStampedUUIDModel):
    profile = models.ForeignKey(
        Profile,
        verbose_name="Usuário",
        related_name="moviment_profiles",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    nf = models.PositiveIntegerField("Nota Fiscal", null=True, blank=True)
    moviment = models.CharField(
        verbose_name="Movimento",
        max_length=1,
        choices=MovimentStatus.choices,
        default=MovimentStatus.INPUT,
    )

    class Meta:
        ordering = ("-pk",)
        db_table = "stocks.moviment"
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"

    def __str__(self):
        return str(self.profile)


class Iten(TimeStampedUUIDModel):
    moviment = models.ForeignKey(
        Moviment,
        verbose_name="Movimento",
        related_name="moviments",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name="Produto",
        related_name="iten_products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    qty = models.PositiveIntegerField("Quantidade", null=True, blank=True)
    stock = models.IntegerField(verbose_name="Estoque")
    detail = models.CharField(
        verbose_name="Detalhe",
        max_length=100,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name="Preço",
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        default="0.00",
    )

    class Meta:
        ordering = ("product", "-pk")
        db_table = "stocks.iten"
        verbose_name = "Iten"
        verbose_name_plural = "Itens"

    def __str__(self):
        return str(self.moviment)
