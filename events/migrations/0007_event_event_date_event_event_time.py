# Generated by Django 4.0.4 on 2022-08-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_category_alter_event_event_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(default='2003-01-02'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default='12:30'),
        ),
    ]
