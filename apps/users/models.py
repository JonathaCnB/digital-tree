from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.forms import photo_size

from apps.common.models import TimeStampedUUIDModel
from apps.core.models import Company


def upload_photo_company(instance, filename):
    return "{0}_{1}/{2}".format(instance.id, instance.user.id, filename)


class User(AbstractUser):
    def __str__(self):
        return self.email

    class Meta:
        db_table = "users.user"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        "User",
        verbose_name="Usuário",
        related_name="user_profiles",
        on_delete=models.PROTECT,
    )
    company = models.ForeignKey(
        Company,
        verbose_name="Companhia",
        related_name="company_profiles",
        on_delete=models.SET_NULL,
        null=True,
    )
    photo_profile = models.ImageField(
        "Foto",
        null=True,
        default="profile_default.png",
        upload_to=upload_photo_company,
        validators=[photo_size],
    )
    aboult = models.TextField()

    class Meta:
        ordering = ("user",)
        db_table = "users.profile"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return str(self.user)
