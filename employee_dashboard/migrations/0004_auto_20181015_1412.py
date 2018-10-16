# Generated by Django 2.1.2 on 2018-10-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_dashboard', '0003_auto_20181015_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_schedule',
            name='priotity',
        ),
        migrations.AddField(
            model_name='user_schedule',
            name='priority',
            field=models.IntegerField(choices=[(1, 'highest'), (2, 'Medium'), (3, 'Lowest')], default=3),
        ),
    ]
