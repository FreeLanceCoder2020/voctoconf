# Generated by Django 2.2.15 on 2020-08-14 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0012_auto_20200814_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 14, 5, 43, 47, 200457)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='end_modified',
            field=models.BooleanField(default=False),
        ),
    ]