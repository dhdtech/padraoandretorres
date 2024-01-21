# Generated by Django 5.0 on 2024-01-20 18:39

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0003_remove_studentcourseagenda_user_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="teacher_name",
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c8c632a9-49b7-4c10-bd47-fb30e65837d8"),
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teachers",
                to="users.user",
                verbose_name="User",
            ),
        ),
        migrations.AlterField(
            model_name="teacherdefaultschedule",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c8c632a9-49b7-4c10-bd47-fb30e65837d8"),
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("c8c632a9-49b7-4c10-bd47-fb30e65837d8"),
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="Id",
            ),
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("c8c632a9-49b7-4c10-bd47-fb30e65837d8"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="users.user",
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
        ),
        migrations.CreateModel(
            name="StudentDefaultSchedule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("c8c632a9-49b7-4c10-bd47-fb30e65837d8"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Id",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("preferred_day", models.IntegerField(verbose_name="Preferred Day")),
                ("preferred_time", models.TimeField(verbose_name="Preferred Time")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_preferences",
                        to="branches.course",
                        verbose_name="Course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_default_schedules",
                        to="users.student",
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student Schedule Preference",
                "verbose_name_plural": "Student Schedule Preferences",
            },
        ),
        migrations.DeleteModel(
            name="StudentSchedulePreference",
        ),
    ]