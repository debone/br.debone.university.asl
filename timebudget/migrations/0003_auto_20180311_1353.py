# Generated by Django 2.0.2 on 2018-03-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timebudget', '0002_auto_20180307_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='frequency',
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('HOME', 'Home'), ('STUDY', 'Study'), ('WORK', 'Work'), ('FUN', 'Fun')], default='HOME', max_length=5),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='day_of_the_week',
            field=models.CharField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=0, max_length=3),
        ),
    ]
