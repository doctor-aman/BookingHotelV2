# Generated by Django 4.0.1 on 2022-01-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('visitorCount', models.IntegerField(blank=True, default=0, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('COMPLETED', 'zavershen'), ('DROPPED', 'udalen')], max_length=10, unique=True)),
            ],
        ),
    ]
