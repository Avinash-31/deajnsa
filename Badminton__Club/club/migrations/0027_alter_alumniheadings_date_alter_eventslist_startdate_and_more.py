# Generated by Django 5.0.2 on 2024-02-17 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0026_eventslist_description2_alter_alumniheadings_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumniheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2024, 2, 17, 19, 18, 30, 290152)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 17, 19, 18, 30, 288554)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2024, 2, 17, 19, 18, 30, 289150)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateField(default=datetime.datetime(2024, 2, 17, 19, 18, 30, 288907)),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='Date',
            field=models.DateField(default=datetime.datetime(2024, 2, 17, 19, 18, 30, 289678)),
        ),
    ]
