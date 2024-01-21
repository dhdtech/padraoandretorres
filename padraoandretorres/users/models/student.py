from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import BaseModel
from core import models as core_models


class Student(BaseModel):
    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="students",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")


class StudentDefaultSchedule(BaseModel):
    student = models.ForeignKey(
        "users.student",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="student_default_schedules",
        null=True,
    )
    course = models.ForeignKey(
        "branches.Course",
        verbose_name=_("Course"),
        on_delete=models.CASCADE,
        related_name="student_preferences",
    )
    day = models.IntegerField(
        verbose_name=_("Preferred Day"),
        blank=False,
        null=False,
        choices=core_models.DayChoices.choices,
    )
    _clone_excluded_fields = ["student"]

    def __str__(self):
        if self.student:
            return f"{self.student.user.first_name} {self.student.user.last_name} - {core_models.get_day_of_week(self.day)} - {self.course.course_name}"
        else:
            return f"CLONE - {core_models.get_day_of_week(self.day)} - {self.course.course_name}"

    class Meta:
        verbose_name = _("Student Schedule Preference")
        verbose_name_plural = _("Student Schedule Preferences")
