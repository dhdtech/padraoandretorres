from core.admin.base import BaseAdmin
from django.contrib import admin
from users import models as user_models


@admin.register(user_models.Teacher)
class TeacherAdmin(BaseAdmin):
    pass


@admin.register(user_models.TeacherDefaultSchedule)
class TeacherDefaultScheduleAdmin(BaseAdmin):
    # Order by
    ordering = [
        "day",
        "course__start_time",
        "teacher__user__first_name",
        "teacher__user__last_name",
    ]
    # Filters
    list_filter = [
        "teacher__user__first_name",
        "teacher__user__last_name",
        "course__course_name",
        "day",
    ]
