# Generated by Django 4.2 on 2024-10-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_servicespage_banner_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='list_item_four',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='list_item_one',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='list_item_three',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='list_item_two',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
