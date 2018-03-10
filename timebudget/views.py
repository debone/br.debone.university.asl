from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TimeslotForm

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'timebudget/index.html')

def timeslot_create(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/timeslot/')
    else:
        form = TimeslotForm()

    return render(request, 'timebudget/form.html', {'form': form})