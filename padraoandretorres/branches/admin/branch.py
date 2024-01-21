from core.admin.base import BaseAdmin
from django.contrib import admin
from branches import models as branches_models


@admin.register(branches_models.Branch)
class BranchAdmin(BaseAdmin):
    pass
