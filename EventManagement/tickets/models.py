from django.db import models
from datetime import datetime
from django.db.models import Q
from django.urls import reverse

class Ticket(models.Model):


    ticket_count = models.IntegerField(blank=True, null=True)
    ticket_date = models.DateField(blank=True, null=True)
    ticket_time = models.TimeField(blank=True, null=True)

    ticket_for_event = models.CharField(max_length=255, blank=True, null=True)
    ticket_for_client = models.CharField(max_length=255, blank=True, null=True)

    #ticket_for_event = models.ForeignKey('event.Event', on_delete=models.CASCADE, blank=True, null=True)
    #ticket_for_client = models.ForeignKey('client.Client', on_delete=models.CASCADE, blank=True, null=True)

    date_added = models.DateTimeField(default=datetime.now, blank=True)
    ticket_username = models.CharField(max_length=255, blank=True, null=True)

    # on submit click on the  entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('home')
