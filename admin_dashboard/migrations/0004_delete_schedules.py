# Generated by Django 2.1.2 on 2018-10-15 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_shift'),
        ('employee_dashboard', '0003_auto_20181015_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedules',
        ),
    ]