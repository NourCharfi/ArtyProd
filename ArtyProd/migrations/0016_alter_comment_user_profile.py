# Generated by Django 4.2.1 on 2023-05-22 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ArtyProd", "0015_merge_20230522_2109"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics"),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("phone_no", models.IntegerField(blank=True, null=True)),
                ("facebook", models.CharField(blank=True, max_length=300, null=True)),
                ("instagram", models.CharField(blank=True, max_length=300, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
