# Generated by Django 4.0.4 on 2022-08-12 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_event_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='event_cat',
        ),
    ]
