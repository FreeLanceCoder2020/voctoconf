# Generated by Django 3.0.7 on 2020-08-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_bans_reason'),
    ]

    operations = [
        migrations.RenameModel('Bans', 'Ban'),
    ]
