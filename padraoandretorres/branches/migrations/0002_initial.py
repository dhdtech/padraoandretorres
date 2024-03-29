# Generated by Django 5.0 on 2024-01-20 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("branches", "0001_initial"),
        ("core", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentcourseagenda",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="course_agendas",
                to="users.user",
                verbose_name="User",
            ),
        ),
        migrations.AddField(
            model_name="studentcourseagenda",
            name="week",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="core.week",
                verbose_name="Week",
            ),
        ),
        migrations.AddField(
            model_name="studentenrollment",
            name="course_schedule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="branches.courseschedule",
                verbose_name="Course Schedule",
            ),
        ),
        migrations.AddField(
            model_name="studentenrollment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollments",
                to="users.user",
                verbose_name="User",
            ),
        ),
    ]
