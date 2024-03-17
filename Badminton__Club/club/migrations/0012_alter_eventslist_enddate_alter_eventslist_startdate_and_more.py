# Generated by Django 4.2.2 on 2023-07-03 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_teamheadings_heading1_alter_eventslist_enddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventslist',
            name='EndDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 24, 8, 552177)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 24, 8, 552161)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 24, 8, 552734)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 24, 8, 552515)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='heading',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]