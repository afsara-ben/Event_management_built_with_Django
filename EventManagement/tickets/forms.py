from django import forms
from .models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('ticket_for_event', 'ticket_count', 'ticket_for_client', 'ticket_date',
                  'ticket_time', 'date_added')

