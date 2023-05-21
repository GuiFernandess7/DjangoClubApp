from django.contrib import admin
from django.urls import path
from events.views import *

urlpatterns = [
    path('', home, name="home"),
    path('events/', all_events, name="event_list"),
]