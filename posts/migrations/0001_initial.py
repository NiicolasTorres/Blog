# Generated by Django 4.1 on 2022-10-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('create_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
