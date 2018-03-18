from django.utils.timezone import now
from datetime import timedelta

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from .models import Timeslot, Event

from .forms import TimeslotForm, EventForm

def index(request):
    timeslots = Timeslot.objects.all().order_by('-start_time')

    try:
        timeslot = Timeslot.objects.filter(
            start_time__lte=now()
        ).order_by('-start_time')[0:1].get()

        if timeslot.start_time + timeslot.duration < now():
            timeslot = False
            timeleft = 0
        else:
            timeleft = timeslot.start_time - now() + timeslot.duration
    except Timeslot.DoesNotExist:
        timeleft = 0
        timeslot = False

    events = Event.objects.filter(
        timeslot=timeslot
    ) if timeslot else False

    return render(request, 'timebudget/index.html', {
        'timeslots': timeslots,
        'timeslot': timeslot,
        'timeleft': timeleft,
        'events': events
    })

def view(request, slot_id):
    timeslot = get_object_or_404(Timeslot, pk=slot_id)

    events = Event.objects.filter(
        timeslot=timeslot
    ) if timeslot else False

    return render(request, 'timebudget/timeslot.html', {
        'timeslot': timeslot,
        'events': events
    })

def create(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TimeslotForm({
            'duration': timedelta(minutes=25)
        })
        # form.save()

    return render(request, 'timebudget/form.html', {'form': form})

def newTask(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        timeslot = request.GET.get('timeslot')

        if not timeslot:
            return HttpResponseRedirect('/')

        form = EventForm(initial={
            'timeslot': timeslot
        })

        return render(request, 'event/newtask.html', {
            'form': form,
            'timeslot_id': timeslot
        })