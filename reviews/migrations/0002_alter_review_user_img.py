# Generated by Django 5.1.1 on 2024-09-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="user_img",
            field=models.ImageField(
                blank=True, default="default.png", upload_to="reviews"
            ),
        ),
    ]
