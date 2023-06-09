# Generated by Django 4.2.1 on 2023-05-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('bank transfer', 'Wire Transfer'), ('credit card', 'Credit Card')], max_length=20)),
                ('payment_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
    ]
