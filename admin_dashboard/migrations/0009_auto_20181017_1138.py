# Generated by Django 2.1.2 on 2018-10-17 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0008_csv_export'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csv_export',
            name='user_schedule_ptr',
        ),
        migrations.DeleteModel(
            name='CSV_export',
        ),
    ]
