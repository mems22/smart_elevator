# Generated by Django 4.1.7 on 2023-04-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Elevator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("floor_request", models.IntegerField()),
                ("elevator_id", models.IntegerField()),
            ],
        ),
    ]
