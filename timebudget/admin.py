from django.contrib import admin

# Register your models here.
from .models import Timeslot, Event

admin.site.register(Timeslot)
admin.site.register(Event)