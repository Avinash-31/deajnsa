# Generated by Django 4.2.2 on 2023-07-03 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_eventslist_google_form_alter_eventslist_enddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamheadings',
            name='heading1',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='EndDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 14, 45, 888252)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='Google_form',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='Location',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='Register_Soon',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 14, 45, 888237)),
        ),
        migrations.AlterField(
            model_name='eventslist',
            name='Title',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 14, 45, 888764)),
        ),
        migrations.AlterField(
            model_name='galleryheadings',
            name='heading',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 13, 14, 45, 888551)),
        ),
        migrations.AlterField(
            model_name='galleryimages',
            name='EventName',
            field=models.TextField(default='all', max_length=50),
        ),
        migrations.AlterField(
            model_name='sponsers',
            name='Link',
            field=models.CharField(blank=True, default='no link', max_length=500),
        ),
        migrations.AlterField(
            model_name='teamheadings',
            name='heading',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Instagram',
            field=models.CharField(blank=True, default='no link', max_length=500),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Linkedin',
            field=models.CharField(blank=True, default='no link', max_length=500),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Name',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='Twitter',
            field=models.CharField(blank=True, default='no link', max_length=500),
        ),
    ]
