# Generated by Django 4.2.1 on 2023-05-14 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ArtyProd", "0005_alter_personnel_statut"),
    ]

    operations = [
        migrations.RemoveField(model_name="personnel", name="statut",),
    ]