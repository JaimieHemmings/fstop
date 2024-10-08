# Generated by Django 5.1.1 on 2024-09-22 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0003_alter_payment_stripe_id"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="name",
        ),
        migrations.AddField(
            model_name="payment",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="profiles.userprofile",
            ),
        ),
    ]
