# Generated by Django 3.2.5 on 2021-08-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_entry_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='operation',
            field=models.CharField(choices=[['PROC', 'PROC - Proccessing'], ['Picking', 'Picking - Scan, Replen , Batch'], ['Break', 'Break - Bathroom, Coffee, 15'], ['LOAD', 'LOAD - Loading the truck'], ['Rec', 'Rec - Receiving'], ['DEL', 'DEL - Delivery'], ['Backstocking', 'Backstocking - *'], ['Cleaning', 'Cleaning - *'], ['Lunch', 'Lunch - *']], max_length=50),
        ),
    ]
