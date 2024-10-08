# Generated by Django 5.1.1 on 2024-09-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_article_exerpt"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="cover_image",
            new_name="slider_image_four",
        ),
        migrations.AddField(
            model_name="article",
            name="slider_image_one",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
        migrations.AddField(
            model_name="article",
            name="slider_image_three",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
        migrations.AddField(
            model_name="article",
            name="slider_image_two",
            field=models.ImageField(blank=True, default="default.png", upload_to=""),
        ),
    ]
