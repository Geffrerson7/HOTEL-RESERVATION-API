# Generated by Django 4.2.1 on 2023-05-11 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roomType', '0002_roomtype_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True)),
                ('floor', models.IntegerField()),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='roomType.roomtype')),
            ],
            options={
                'db_table': 'Room',
            },
        ),
    ]