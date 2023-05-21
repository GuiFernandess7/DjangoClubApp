from django.shortcuts import render
from .models import Event

def home(request):
    return render(request, 'events/home.html', {})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', 
                  {"event_list": events})