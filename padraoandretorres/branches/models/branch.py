from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import BaseModel


class Branch(BaseModel):
    name = models.CharField(
        verbose_name=_("Nome Filial"), max_length=255, blank=False, null=False
    )
    location = models.CharField(
        verbose_name=_("Endereço"), max_length=255, blank=False, null=False
    )

    def __str__(self):
        return f"{self.name} - {self.location}"

    class Meta:
        verbose_name = _("Filial")
        verbose_name_plural = _("Filiais")
