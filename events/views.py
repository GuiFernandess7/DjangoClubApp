from django.shortcuts import render, redirect
from .models import *
from .forms import VenueForm, EventForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, FileResponse
from django.core.paginator import Paginator
import csv

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# Generate a PDF venue list
def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    text_obj = c.beginText()
    text_obj.setTextOrigin(inch, inch)
    text_obj.setFont("Helvetica", 14)
    venues = Venue.objects.all()

    lines = []
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")
    
    for line in lines:
        text_obj.textLine(line)

    c.drawText(text_obj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

# Generate text file venue list
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=venues.csv"
    venues = Venue.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])

    for venue in venues:
        writer.writerow([venue.name,
        venue.address,
        venue.zip_code,
        venue.phone,
        venue.web,
        venue.email_address])

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

    p = Paginator(Venue.objects.all(), 1) # Venue by page
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "" * venues.paginator.num_pages

    return render(request, 'events/venues.html', 
                  {'venue_list': venue_list,
                   'venues': venues,
                   'nums': nums
                })

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
    
    