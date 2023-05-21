from django.contrib import admin
from django.urls import path
from events.views import *

urlpatterns = [
    path('', home, name="home"),
    path('events/', all_events, name="event-list"),
    path('add_venue', add_venue, name='add-venue'),
    path('venues', list_venues, name="list-venues"),
    path('show_venue/<venue_id>', show_venue, name="show-venue"),
]