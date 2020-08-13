# Generated by Django 2.2.15 on 2020-08-13 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('name_modified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('date_modified', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=1800, verbose_name='Duration (seconds)')),
                ('duration_modified', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('title_modified', models.BooleanField(default=False)),
                ('room_modified', models.BooleanField(default=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventpage.Room')),
            ],
        ),
    ]
