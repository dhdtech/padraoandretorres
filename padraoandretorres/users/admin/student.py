from django.contrib import admin
from core.admin.base import BaseAdmin
from users import models as user_models


@admin.register(user_models.Student)
class StudentAdmin(BaseAdmin):
    pass


@admin.register(user_models.StudentDefaultSchedule)
class StudentDefaultScheduleAdmin(BaseAdmin):
    # Order by
    ordering = [
        "student__user__first_name",
        "student__user__last_name",
        "day",
        "course__start_time",
        "course__course_name",
    ]

    # Filters
    list_filter = [
        "student__user__first_name",
        "student__user__last_name",
        "course__course_name",
        "day",
    ]
