import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import BaseModel


class DayChoices(models.IntegerChoices):
    MONDAY = 0, _("Monday")
    TUESDAY = 1, _("Tuesday")
    WEDNESDAY = 2, _("Wednesday")
    THURSDAY = 3, _("Thursday")
    FRIDAY = 4, _("Friday")
    SATURDAY = 5, _("Saturday")
    SUNDAY = 6, _("Sunday")


class Week(BaseModel):
    year = models.IntegerField(verbose_name=_("Year"), blank=False, null=False)
    week_number = models.IntegerField(
        verbose_name=_("Week Number"), blank=False, null=False
    )
    _clone_fields = ["week_number"]

    def __str__(self):
        return f"Week {self.week_number}, {self.year}"

    class Meta:
        verbose_name = _("Week")
        verbose_name_plural = _("Weeks")
        unique_together = ["year", "week_number"]


def get_day_of_week(day):
    return DayChoices(day).name
