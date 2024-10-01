# Generated by Django 4.2 on 2024-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepageabout_homepage_about_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageTrustedBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trusted_by_title', models.CharField(default='Enter a Title', max_length=100)),
                ('trusted_by_lead', models.CharField(default='Enter a Lead', max_length=200)),
                ('img_one', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_two', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_three', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_four', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_five', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_six', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_seven', models.ImageField(default='default.png', upload_to='cms/home/')),
                ('img_eight', models.ImageField(default='default.png', upload_to='cms/home/')),
            ],
        ),
    ]
