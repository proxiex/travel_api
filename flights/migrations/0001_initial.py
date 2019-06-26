""" """

# Generated by Django 2.2.2 on 2019-06-13 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Airline Name')),
                ('flight_number', models.CharField(max_length=100, verbose_name='Flight Numbrer')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=100, verbose_name='From Location')),
                ('to_location', models.CharField(max_length=100, verbose_name='To Location')),
                ('departure_time', models.DateTimeField(verbose_name='Departure time')),
                ('arrival_time', models.DateTimeField(verbose_name='Arrival Time')),
                ('no_of_seats', models.IntegerField()),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Airline')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
