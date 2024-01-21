# Generated by Django 5.0 on 2024-01-20 18:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("58b1f6b1-64b5-457b-b589-014381480ede"),
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
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email Address"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=100, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=100, verbose_name="Last Name"),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("58b1f6b1-64b5-457b-b589-014381480ede"),
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
                    "teacher_name",
                    models.CharField(max_length=255, verbose_name="Teacher Name"),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teachers",
                        to="branches.branch",
                        verbose_name="Branch",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teachers",
                        to="users.user",
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
            },
        ),
        migrations.CreateModel(
            name="TeacherDefaultSchedule",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("58b1f6b1-64b5-457b-b589-014381480ede"),
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
                ("default_day", models.IntegerField(verbose_name="Default Day")),
                ("default_time", models.TimeField(verbose_name="Default Time")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teacher_schedules",
                        to="branches.course",
                        verbose_name="Course",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="default_schedules",
                        to="users.teacher",
                        verbose_name="Teacher",
                    ),
                ),
            ],
            options={
                "verbose_name": "Teacher Default Schedule",
                "verbose_name_plural": "Teacher Default Schedules",
            },
        ),
        migrations.CreateModel(
            name="StudentSchedulePreference",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("58b1f6b1-64b5-457b-b589-014381480ede"),
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
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedule_preferences",
                        to="users.user",
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student Schedule Preference",
                "verbose_name_plural": "Student Schedule Preferences",
            },
        ),
    ]
