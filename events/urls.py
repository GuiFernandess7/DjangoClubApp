from django.contrib import admin
from django.urls import path
from events.views import *

urlpatterns = [
    path('', home, name="home"),
    path('events/', all_events, name="event-list"),
    path('add_venue', add_venue, name='add-venue'),
    path('add_event', add_event, name='add-event'),
    path('venues', list_venues, name="list-venues"),
    path('show_venue/<venue_id>', show_venue, name="show-venue"),
    path('search_venues', search_venue, name="search-venues"),
    path('update_venue/<venue_id>', update_venue, name="update-venue"),
    path('update_event/<event_id>', update_event, name="update-event"),
    path('delete_event/<event_id>', delete_event, name='delete-event'),
    path('delete_venue/<venue_id>', delete_venue, name='delete-venue'),

]