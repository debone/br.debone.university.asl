from django import forms

from .models import Timeslot, Event

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['duration']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['timeslot', 'type', 'name']
        widgets = {'timeslot': forms.HiddenInput()}