# Generated by Django 2.0.5 on 2019-07-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_agencybrief_agency_budget_lower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencybrief',
            name='agency_budget_lower',
            field=models.BigIntegerField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agencybrief',
            name='agency_budget_upper',
            field=models.BigIntegerField(blank=True, default=None, max_length=255, null=True),
        ),
    ]