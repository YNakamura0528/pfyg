# Generated by Django 2.1.3 on 2018-11-22 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=150)),
                ('taskImportance', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=1024, null=True)),
                ('createdDatetime', models.DateTimeField(auto_now_add=True)),
                ('updatedDatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
