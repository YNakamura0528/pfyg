# Generated by Django 2.1.3 on 2018-11-23 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_donedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
