# Generated by Django 5.1.1 on 2024-09-22 14:55

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                    "profile_pic",
                    models.ImageField(
                        blank=True,
                        default="profile_pics/default.png",
                        upload_to="profile_pics",
                    ),
                ),
                ("fname", models.CharField(blank=True, max_length=50, null=True)),
                ("lname", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                ("postcode", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "town_or_city",
                    models.CharField(blank=True, max_length=40, null=True),
                ),
                (
                    "street_address1",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                (
                    "street_address2",
                    models.CharField(blank=True, max_length=80, null=True),
                ),
                ("county", models.CharField(blank=True, max_length=80, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
