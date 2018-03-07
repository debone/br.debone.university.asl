from django.db import models

# Create your models here.
class Timeslot(models.Model):
    startTime = models.IntegerField()
    dayOfTheWeek = models.IntegerField()
    duration = models.IntegerField()

class Event(models.Model):
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()