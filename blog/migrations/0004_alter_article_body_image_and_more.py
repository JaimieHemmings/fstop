# Generated by Django 5.1.1 on 2024-09-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_rename_cover_image_article_slider_image_four_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="body_image",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="slider_image_four",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="slider_image_one",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="slider_image_three",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="slider_image_two",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
    ]
