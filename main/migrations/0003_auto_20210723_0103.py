# Generated by Django 3.2.5 on 2021-07-23 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_worksheet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='start_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
