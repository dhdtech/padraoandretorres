# Generated by Django 5.0 on 2024-01-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branches", "0007_remove_course_duration"),
        ("users", "0005_remove_teacherdefaultschedule_default_day_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="teacherdefaultschedule",
            unique_together={("teacher", "course", "day")},
        ),
        migrations.AlterField(
            model_name="teacherdefaultschedule",
            name="day",
            field=models.IntegerField(
                choices=[
                    (0, "Monday"),
                    (1, "Tuesday"),
                    (2, "Wednesday"),
                    (3, "Thursday"),
                    (4, "Friday"),
                    (5, "Saturday"),
                    (6, "Sunday"),
                ],
                verbose_name="Day",
            ),
        ),
        migrations.RemoveField(
            model_name="teacherdefaultschedule",
            name="time",
        ),
    ]