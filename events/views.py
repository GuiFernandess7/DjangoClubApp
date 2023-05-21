from django.shortcuts import render, redirect
from .models import *
from .forms import VenueForm

def home(request):
    return render(request, 'events/home.html', {})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', 
                  {"event_list": events})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/add_venue?submitted=True")
    else:
        if 'submitted' in request.GET:
            submitted = True
        form = VenueForm()

    context = {
        'form': form,
        'submitted': submitted
    }
    form = VenueForm()
    return render(request, 'events/add_venue.html', context)

def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venues.html', 
                  {'venue_list': venue_list})

def show_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'events/show_venue.html', 
                  {'venue': venue})
