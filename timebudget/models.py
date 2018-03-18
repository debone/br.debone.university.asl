from django.utils.timezone import now
from django.db import models

# Create your models here.
class Timeslot(models.Model):
    start_time = models.DateTimeField(default=now)
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