# Generated by Django 4.2 on 2024-10-11 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepagepanel_link_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagehero',
            name='hero_image_mobile',
        ),
    ]
