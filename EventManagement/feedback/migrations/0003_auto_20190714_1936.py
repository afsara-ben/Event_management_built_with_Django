# Generated by Django 2.0.5 on 2019-07-14 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20190714_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='email',
            new_name='customer_email',
        ),
        migrations.AddField(
            model_name='feedback',
            name='agency_name',
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
    ]