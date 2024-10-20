# Generated by Django 4.2 on 2024-10-11 09:00

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_homepagepanel_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagepanel',
            name='icon',
        ),
        migrations.AddField(
            model_name='homepagepanel',
            name='image',
            field=models.ImageField(default='default.png', upload_to=home.models.HomePagePanel.get_path),
        ),
        migrations.AddField(
            model_name='homepagepanel',
            name='image_alt',
            field=models.CharField(default='Enter an alt text', max_length=100),
        ),
    ]
