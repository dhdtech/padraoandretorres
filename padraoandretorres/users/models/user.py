from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import BaseModel


class User(BaseModel):
    email = models.EmailField(
        verbose_name=_("Email Address"),
        blank=False,
        null=False,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_("First Name"), max_length=100, blank=False, null=False
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"), max_length=100, blank=False, null=False
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
