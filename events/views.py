from django.shortcuts import render, redirect
from .models import *
from .forms import VenueForm, EventForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Generate text file venue list
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = "attachment; filename=venues.txt"
    venues = Venue.objects.all()
    
    lines = []
    for venue in venues:
        lines.append(f"""{venue.name}\n
        {venue.address}\n
        {venue.zip_code}\n
        {venue.phone}\n
        {venue.web}\n
        {venue.email_address}\n\n""")
        
    response.writelines(lines)
    return response

def home(request):
    return render(request, 'events/home.html', {})

def all_events(request):
    events = Event.objects.all().order_by('name')
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

def search_venue(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        if searched:
            venues = Venue.objects.filter(name__icontains=searched)
        else:
            venues = Venue.objects.none()  # Retorna uma QuerySet vazia
        return render(request, 'events/search_venues.html', 
                      {'searched': searched,
                       'venues': venues})
    else:
        return render(request, 'events/show_venue.html', {})

def update_venue(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    
    return render(request, 'events/update_venue.html', 
                  {'venue': venue, 'form': form})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/add_event?submitted=True")
    else:
        if 'submitted' in request.GET:
            submitted = True
        form = EventForm()

    context = {
        'form': form,
        'submitted': submitted
    }
    form = EventForm()
    return render(request, 'events/add_event.html', context)

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event-list')
    
    return render(request, 'events/update_event.html', 
                  {'event': event, 'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('event-list')  
    
def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    venue.delete()
    return redirect('list-venues')  
    
    