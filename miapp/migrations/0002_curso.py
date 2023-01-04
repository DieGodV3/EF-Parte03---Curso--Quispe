# Generated by Django 4.1.5 on 2023-01-04 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "codigo",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("nombre", models.CharField(max_length=20)),
                ("horas", models.CharField(max_length=5)),
                ("credito", models.CharField(max_length=20)),
                (
                    "Fecha_registro",
                    models.DateTimeField(verbose_name="Fecha de nacimiento"),
                ),
                ("estado", models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name="docente",
            name="fecha_registro",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2023, 1, 4, 12, 3, 45, 103750)
            ),
        ),
    ]