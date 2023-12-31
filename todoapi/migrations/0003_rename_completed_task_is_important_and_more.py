# Generated by Django 4.2.3 on 2023-07-08 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0002_alter_task_id_alter_task_task_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed',
            new_name='is_important',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='important',
            new_name='task_completed',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created_at',
            new_name='task_created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='updated_at',
            new_name='task_updated_at',
        ),
        migrations.AddField(
            model_name='task',
            name='task_due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 12, 54, 55, 583452)),
        ),
    ]
