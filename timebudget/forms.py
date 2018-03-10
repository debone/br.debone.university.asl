from django.forms import ModelForm
from .models import Timeslot

class TimeslotForm(ModelForm):
    class Meta:
        model = Timeslot
        fields = ['start_time', 'day_of_the_week', 'duration']