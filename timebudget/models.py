from django.db import models

# Create your models here.
class Timeslot(models.Model):
    startTime = models.IntegerField()
    dayOfTheWeek = models.IntegerField()
    duration = models.IntegerField()
