# Generated by Django 4.1.7 on 2023-04-01 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("elevator", "0003_alter_systemconfig_no_elevators_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="elevator",
            name="elevator_id",
        ),
    ]
