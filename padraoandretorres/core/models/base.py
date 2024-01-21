import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_clone import CloneMixin


class BaseModel(CloneMixin, models.Model):
    id = models.UUIDField(
        verbose_name=_("Id"),
        editable=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        editable=False,
        blank=False,
        null=False,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
