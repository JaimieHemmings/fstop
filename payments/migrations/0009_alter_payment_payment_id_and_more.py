# Generated by Django 4.2 on 2024-10-15 15:40

from django.db import migrations, models
import payments.models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_payment_country_alter_payment_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(default=payments.models.Payment._generate_payment_id, editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='payment',
            name='street_address2',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
    ]
