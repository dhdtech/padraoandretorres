from django.contrib import admin
from core.models.core import Week
from model_clone import CloneModelAdmin


class BaseAdmin(CloneModelAdmin, admin.ModelAdmin):
    pass
