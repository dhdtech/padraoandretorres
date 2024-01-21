from django.contrib import admin
from core.models.core import Week
from core.admin.base import BaseAdmin


@admin.register(Week)
class WeekAdmin(BaseAdmin):
    pass
