# Generated by Django 4.1 on 2022-10-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='finished',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
