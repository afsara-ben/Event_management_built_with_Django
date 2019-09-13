from django import forms
from .models import *


class EventCreate(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_venue', 'event_type', 'event_budget', 'event_guest_number', 'event_description',)


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_budget', 'event_guest_number', 'event_date', 'event_client', 'event_time',
                  'event_remote_arrange', 'event_size', 'event_description', )

