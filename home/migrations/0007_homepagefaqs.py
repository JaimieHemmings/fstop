# Generated by Django 4.2 on 2024-10-01 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepagetrustedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageFAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_question', models.CharField(max_length=100)),
                ('faq_answer', models.TextField()),
            ],
        ),
    ]
