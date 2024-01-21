from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models.base import BaseModel
from core import models as core_models


class Teacher(BaseModel):
    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="teachers",
    )
    branch = models.ForeignKey(
        "branches.Branch",
        verbose_name=_("Branch"),
        on_delete=models.CASCADE,
        related_name="teachers",
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")


class TeacherDefaultSchedule(BaseModel):
    teacher = models.ForeignKey(
        "users.Teacher",
        verbose_name=_("Teacher"),
        on_delete=models.CASCADE,
        related_name="default_schedules",
    )
    course = models.ForeignKey(
        "branches.Course",
        verbose_name=_("Course"),
        on_delete=models.CASCADE,
        related_name="teacher_schedules",
    )
    day = models.IntegerField(
        verbose_name=_("Day"),
        blank=False,
        null=False,
        choices=core_models.DayChoices.choices,
    )

    def __str__(self):
        return f"{self.full_name} - {self.course.course_name} - {core_models.get_day_of_week(self.day)}"

    @property
    def full_name(self):
        return f"{self.teacher.user.first_name} {self.teacher.user.last_name}"

    class Meta:
        verbose_name = _("Teacher Default Schedule")
        verbose_name_plural = _("Teacher Default Schedules")
        unique_together = ["teacher", "course", "day"]
