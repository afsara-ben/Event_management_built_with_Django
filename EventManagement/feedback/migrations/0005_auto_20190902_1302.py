# Generated by Django 2.2.3 on 2019-09-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20190714_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='behaviour',
            field=models.IntegerField(blank=True, choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='overall',
            field=models.IntegerField(blank=True, choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='price_fairness',
            field=models.IntegerField(blank=True, choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='professionalism',
            field=models.IntegerField(blank=True, choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1, null=True),
        ),
    ]
