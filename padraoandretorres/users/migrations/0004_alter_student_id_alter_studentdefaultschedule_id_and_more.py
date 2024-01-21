# Generated by Django 5.0 on 2024-01-20 18:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_student_id_alter_studentdefaultschedule_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="studentdefaultschedule",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="teacherdefaultschedule",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Id",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Id",
            ),
        ),
    ]