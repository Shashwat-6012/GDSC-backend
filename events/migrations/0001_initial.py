# Generated by Django 4.0.4 on 2022-08-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('event_state', models.CharField(max_length=50)),
                ('event_location', models.CharField(max_length=200)),
                ('event_organizer', models.CharField(max_length=50)),
            ],
        ),
    ]