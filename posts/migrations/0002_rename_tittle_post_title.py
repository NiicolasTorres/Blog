# Generated by Django 4.1 on 2022-10-08 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
    ]
