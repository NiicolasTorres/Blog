# Generated by Django 4.1 on 2022-10-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Morgoth.jpg', upload_to=''),
        ),
    ]
