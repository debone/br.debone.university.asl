from django.db import models

# Create your models here.
class Timeslot(models.Model):
    DAYS_OF_THE_WEEK = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday')
    )
    start_time = models.TimeField(default='09:00:00')
    day_of_the_week = models.CharField(default='SUN', max_length=3, choices=DAYS_OF_THE_WEEK)
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