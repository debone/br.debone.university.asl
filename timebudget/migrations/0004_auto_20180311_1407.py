# Generated by Django 2.0.2 on 2018-03-11 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timebudget', '0003_auto_20180311_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='day_of_the_week',
            field=models.CharField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1, max_length=3),
        ),
    ]
