# Generated by Django 4.1.2 on 2022-12-22 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('post', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime(2022, 12, 22, 14, 1, 23, 751040))),
            ],
            options={
                'verbose_name': 'User Post',
            },
        ),
    ]
