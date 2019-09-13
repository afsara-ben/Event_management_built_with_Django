# Generated by Django 2.2.3 on 2019-07-28 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_count', models.IntegerField(blank=True, null=True)),
                ('ticket_date', models.DateField(blank=True, null=True)),
                ('ticket_time', models.TimeField(blank=True, null=True)),
                ('ticket_for_event', models.CharField(blank=True, max_length=255, null=True)),
                ('ticket_for_client', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ticket_username', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]