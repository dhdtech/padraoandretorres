from core.admin.base import BaseAdmin
from django.contrib import admin
from users import models as user_models


@admin.register(user_models.User)
class UserAdmin(BaseAdmin):
    pass
