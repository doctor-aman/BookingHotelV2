# Generated by Django 3.2.9 on 2022-01-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]
