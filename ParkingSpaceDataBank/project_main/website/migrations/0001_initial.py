# Generated by Django 4.0.4 on 2022-06-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=120, verbose_name='Car Name')),
                ('car_manufacturer', models.CharField(max_length=120, verbose_name='Car Manufacturer')),
                ('car_color', models.CharField(max_length=120, verbose_name='Car Color')),
                ('plate_num', models.CharField(max_length=20, verbose_name='Plate Number')),
            ],
        ),
    ]
