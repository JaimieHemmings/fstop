# Generated by Django 4.2 on 2024-10-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesbanner',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannerone',
            name='stat_one',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannerone',
            name='stat_one_description',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannerone',
            name='stat_two',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannerone',
            name='stat_two_description',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannertwo',
            name='stat_one',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannertwo',
            name='stat_one_description',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannertwo',
            name='stat_two',
        ),
        migrations.RemoveField(
            model_name='servicescontextbannertwo',
            name='stat_two_description',
        ),
        migrations.AlterField(
            model_name='servicescards',
            name='icon',
            field=models.CharField(max_length=2000),
        ),
    ]
