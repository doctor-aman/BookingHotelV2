# Generated by Django 3.2.9 on 2022-01-15 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('hotel_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='hotel.hotel')),
            ],
        ),
    ]
