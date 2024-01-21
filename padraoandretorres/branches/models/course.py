from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core import models as core_models


class Course(BaseModel):
    branch = models.ForeignKey(
        "branches.Branch",
        verbose_name=_("Branch"),
        on_delete=models.CASCADE,
        related_name="courses",
    )
    course_name = models.CharField(
        verbose_name=_("Course Name"), max_length=255, blank=False, null=False
    )
    start_time = models.TimeField(verbose_name=_("Start Time"), blank=False, null=False)

    def __str__(self):
        return f"{self.branch.name} - {self.course_name}"

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        unique_together = ["branch", "course_name", "start_time"]

        ordering = [
            "branch__name",
            "start_time",
            "course_name",
        ]


class CourseSchedule(BaseModel):
    course = models.ForeignKey(
        "branches.Course",
        verbose_name=_("Course"),
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    week = models.ForeignKey(
        "core.Week",
        verbose_name=_("Week"),
        on_delete=models.CASCADE,
        related_name="course_schedules",
    )
    day_of_week = models.IntegerField(
        verbose_name=_("Day of Week"),
        blank=False,
        null=False,
        choices=core_models.DayChoices.choices,
    )
    active_slots = models.IntegerField(
        verbose_name=_("Active Slots"), blank=False, null=False
    )

    def __str__(self):
        return f"{self.course.course_name} Schedule for Week {self.week.week_number} - {self.course.branch.name}"

    class Meta:
        verbose_name = _("Course Schedule")
        verbose_name_plural = _("Course Schedules")


class StudentEnrollment(BaseModel):
    student = models.ForeignKey(
        "users.Student",
        verbose_name=_("Student"),
        on_delete=models.CASCADE,
        related_name="student_enrollments",
    )
    course_schedule = models.ForeignKey(
        CourseSchedule,
        verbose_name=_("Course Schedule"),
        on_delete=models.CASCADE,
        related_name="student_course_schedule_enrollments",
    )

    def __str__(self):
        return f"{self.student.user.email} - Enrollment in {self.course_schedule.course.course_name}"

    class Meta:
        verbose_name = _("Student Enrollment")
        verbose_name_plural = _("Student Enrollments")


class TeacherEnrollment(BaseModel):
    student = models.ForeignKey(
        "users.Teacher",
        verbose_name=_("Teacher"),
        on_delete=models.CASCADE,
        related_name="teacher_enrollments",
    )
    course_schedule = models.ForeignKey(
        CourseSchedule,
        verbose_name=_("Course Schedule"),
        on_delete=models.CASCADE,
        related_name="teacher_course_schedule_enrollments",
    )

    def __str__(self):
        return f"{self.teacher.user.email} - Enrollment in {self.course_schedule.course.course_name}"

    class Meta:
        verbose_name = _("Teacher Enrollment")
        verbose_name_plural = _("Teacher Enrollments")


# class StudentCourseAgenda(BaseModel):
#     student = models.ForeignKey(
#         "users.Student",
#         verbose_name=_("User"),
#         on_delete=models.CASCADE,
#         related_name="student_course_agendas",
#     )
#     course_schedule = models.ForeignKey(
#         "branches.CourseSchedule",
#         verbose_name=_("Course Schedule"),
#         on_delete=models.CASCADE,
#         related_name="student_agendas",
#     )
#     week = models.ForeignKey(
#         "core.Week",
#         verbose_name=_("Week"),
#         on_delete=models.CASCADE,
#     )
#     day_of_week = models.IntegerField(
#         verbose_name=_("Day of Week"), blank=False, null=False
#     )
#     course_date = models.DateField(
#         verbose_name=_("Course Date"), blank=False, null=False
#     )

#     def __str__(self):
#         return f"{self.student.user.email} - Agenda for {self.course_schedule.course.course_name} on {self.course_date}"

#     class Meta:
#         verbose_name = _("Student Course Agenda")
#         verbose_name_plural = _("Student Course Agendas")
