from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels = {'name': "",
                   'address': "",
                   'zip_code': "",
                   'phone': "",
                   'web': "",
                   'email_address': ""
                }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Venue Name"}),
                   'address': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Address"}),
                   'zip_code': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Zip Code"}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Phone"}),
                   'web': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Web Address"}),
                   'email_address': forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Email"})}

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        labels = {'name': "",
                   'event_date': "YYYY-MM-DD HH:mm:ss",
                   'venue': "Venue:",
                   'manager': "Manager",
                   'description': "",
                   'attendees': "Attendees",
                }
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "event Name"}),
                   'event_date': forms.TextInput(attrs={'class': 'form-control', "placeholder": "event date"}),
                   'venue': forms.Select(attrs={'class': 'form-select', "placeholder": "venue"}),
                   'manager': forms.Select(attrs={'class': 'form-select', "placeholder": "manager"}),
                   'attendees': forms.SelectMultiple(attrs={'class': 'form-control', "placeholder": "attendees"}),
                   'description': forms.Textarea(attrs={'class': 'form-control', "placeholder": "descritpion"}),
        }

