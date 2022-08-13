from django import forms
from .models import Event

class Myform(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_cat","event_name", "event_city", "event_location", "event_organizer","event_details", "event_date", "event_time", "event_image"]
        labels = {"event_cat": "Event Category",
        "event_name": 'Event name', "event_city": "Event's City",
        "event_details": 'Event details',
        "event_location": 'Event location', "event_organizer": 'Event Organizers name', 
        "event_date": 'Event date', "event_time": 'Event time',
        "event_image": 'Event front image'}