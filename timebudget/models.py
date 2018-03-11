from django.db import models

# Create your models here.
class Timeslot(models.Model):
    DAYS_OF_THE_WEEK = (
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday')
    )
    start_time = models.TimeField(default='09:00:00')
    day_of_the_week = models.IntegerField(default=1, max_length=1, choices=DAYS_OF_THE_WEEK)
    duration = models.DurationField()

class Event(models.Model):
    EVENT_TYPE = (
        ('HOME', 'Home'),
        ('STUDY', 'Study'),
        ('WORK', 'Work'),
        ('FUN', 'Fun')
    )
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    type = models.CharField(default='HOME', max_length=5, choices=EVENT_TYPE)
    name = models.CharField(max_length=100)