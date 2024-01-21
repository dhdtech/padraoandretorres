from core.admin.base import BaseAdmin
from branches import models as branches_models
from django.contrib import admin


@admin.register(branches_models.Course)
class CourseAdmin(BaseAdmin):
    pass


@admin.register(branches_models.CourseSchedule)
class CourseScheduleAdmin(BaseAdmin):
    # order by
    ordering = ["week__week_number", "course__start_time", "course__branch__name"]

    # Displayed fields
    list_display = [
        "course",
        "day_of_week",
        "week",
        "active_slots",
    ]

    # Filters
    list_filter = [
        "course__branch",
        "course__course_name",
        "day_of_week",
        "week",
    ]


@admin.register(branches_models.StudentEnrollment)
class StudentEnrollmentAdmin(BaseAdmin):
    pass


@admin.register(branches_models.TeacherEnrollment)
class TeacherEnrollmentAdmin(BaseAdmin):
    pass


# @admin.register(branches_models.StudentCourseAgenda)
# class StudentCourseAgendaAdmin(BaseAdmin):
#     pass
