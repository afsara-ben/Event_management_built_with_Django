# Generated by Django 2.0.5 on 2019-07-13 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_auto_20190713_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agencybrief',
            old_name='agency_budget_lower',
            new_name='agency_event_budget',
        ),
        migrations.RemoveField(
            model_name='agencybrief',
            name='agency_budget_upper',
        ),
    ]
