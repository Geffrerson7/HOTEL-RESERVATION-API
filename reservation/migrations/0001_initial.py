# Generated by Django 4.2.1 on 2023-05-11 04:12

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import reservation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('status', enumfields.fields.EnumField(enum=reservation.models.ReservationStatus, max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_method', models.CharField(max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'Rerervation',
            },
        ),
    ]