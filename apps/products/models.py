from django.db import models
from django.db.models import Q
from django.urls import reverse_lazy

from apps.common.models import TimeStampedUUIDModel
from apps.core.models import Company
from apps.users.models import Profile


class SubGroup(TimeStampedUUIDModel):
    name = models.CharField(
        verbose_name="Sub Grupo",
        max_length=255,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        Company,
        verbose_name="Companhia",
        related_name="sub_groups",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("name",)
        db_table = "products.sub_group"
        verbose_name = "Sub Grupo"
        verbose_name_plural = "Sub Grupos"

    def __str__(self):
        return self.name


class Group(TimeStampedUUIDModel):
    name = models.CharField(verbose_name="Grupo", max_length=255)
    company = models.ForeignKey(
        Company,
        verbose_name="Companhia",
        related_name="groups",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("name",)
        db_table = "products.group"
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.name


class UnitStatus(models.TextChoices):
    UNIT = "und", "Unidade"
    BOX = "b", "Caixa"
    GRAM = "g", "Grama"
    KILOGRAM = "kg", "Quilograma"


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def is_active(self, company):
        return self.get_queryset().is_active(company=company)

    def search(self, company, query=None):
        return self.get_queryset().search(company, query)


class ProductQuerySet(models.QuerySet):
    def is_active(self, company):
        qs = self.select_related("company")
        qs = qs.filter(company=company, is_active=True)
        return qs

    def search(self, company, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(product__icontains=query) | Q(barcode__icontains=query)
        qs = self.is_active(company)
        qs = qs.filter(lookups)
        return qs


class Product(TimeStampedUUIDModel):
    product = models.CharField(verbose_name="Produto", max_length=255)
    price = models.DecimalField(
        verbose_name="Preço",
        max_digits=7,
        decimal_places=2,
    )
    stock = models.IntegerField(verbose_name="Estoque atual", default=0)
    minimum_stock = models.PositiveIntegerField(
        verbose_name="estoque mínimo",
        default=0,
    )
    unit = models.CharField(
        max_length=3,
        verbose_name="Unidade",
        choices=UnitStatus.choices,
        default=UnitStatus.UNIT,
    )
    barcode = models.CharField(
        verbose_name="Código de Barras",
        max_length=50,
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        to="Group",
        verbose_name="Grupo",
        on_delete=models.SET_NULL,
        related_name="groups",
        null=True,
        blank=True,
    )
    sub_group = models.ForeignKey(
        to="SubGroup",
        verbose_name="Sub Grupo",
        on_delete=models.SET_NULL,
        related_name="sub_groups",
        null=True,
        blank=True,
    )
    profile = models.ForeignKey(
        Profile,
        verbose_name="Usuário",
        related_name="profiles",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        Company,
        verbose_name="Companhia",
        related_name="companies",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    objects = ProductManager()

    @property
    def stock_percentage(self):
        percentage = (self.stock / self.minimum_stock) * 100
        if percentage > 50:
            status = 'good'
        elif percentage > 25:
            status = 'warning'
        else:
            status = 'danger'
        return f'{round(percentage,1)}%', status

    class Meta:
        ordering = ("product",)
        db_table = "products.product"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse_lazy("products:detail", kwargs={"pk": self.pk})
