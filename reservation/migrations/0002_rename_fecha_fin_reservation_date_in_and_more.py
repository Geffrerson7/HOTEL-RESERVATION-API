# Generated by Django 4.2.1 on 2023-05-11 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='fecha_fin',
            new_name='date_in',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='fecha_inicio',
            new_name='date_out',
        ),
    ]
