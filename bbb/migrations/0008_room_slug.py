# Generated by Django 3.0.8 on 2020-08-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0007_room_hangout_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, max_length=35, null=True),
        ),
    ]