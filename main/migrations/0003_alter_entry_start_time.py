# Generated by Django 3.2.5 on 2021-07-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_entry_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]