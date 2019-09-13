# Generated by Django 2.0.5 on 2019-07-21 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_auto_20190721_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor_info',
            old_name='vendor_specialty',
            new_name='vendor_name',
        ),
        migrations.AddField(
            model_name='vendor_info',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
