from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField, BRStateField
from utils.forms import photo_size

from apps.common.models import TimeStampedUUIDModel


def upload_photo_company(instance, filename):
    return "{0}_{1}/{2}".format(instance.id, instance.company, filename)


class Company(TimeStampedUUIDModel):
    company = models.CharField("Empresa", max_length=250)
    cnpj = BRCNPJField("CNPJ", default="", null=True)
    postal_code = BRPostalCodeField("CEP", default="")
    email = models.EmailField("E-mail", default="")
    address = models.CharField("Endereço", max_length=250, default="")
    cell_phone = models.CharField(
        "Telefone Celular",
        max_length=250,
        default="",
        blank=True,
    )
    number = models.CharField("Número", max_length=10, default="")
    complement = models.CharField(
        "Complemento",
        max_length=20,
        default="",
        blank=True,
        null=True,
    )
    district = models.CharField("Bairro", max_length=100, default="")
    state = BRStateField("Estado", default="")
    city = models.CharField("Cidade", max_length=100, default="")
    photo_profile = models.ImageField(
        "Foto",
        null=True,
        default="profile_default.png",
        upload_to=upload_photo_company,
        validators=[photo_size],
    )

    class Meta:
        ordering = ("company",)
        db_table = "core.company"
        verbose_name = "Companhia"
        verbose_name_plural = "Companhias"

    def __str__(self):
        return self.company
