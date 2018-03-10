from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from .models import Timeslot

from .forms import TimeslotForm

def index(request):
    timeslots = Timeslot.objects.all()
    return render(request, 'timebudget/index.html', {'timeslots': timeslots})

def view(request, slot_id):
    timeslot = get_object_or_404(Timeslot, pk=slot_id)

    return render(request, 'timebudget/timeslot.html', {'timeslot': timeslot})

def create(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/timeslot/')
    else:
        form = TimeslotForm()

    return render(request, 'timebudget/form.html', {'form': form})