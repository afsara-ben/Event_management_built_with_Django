from django.db import models
from django.urls import reverse


class Event(models.Model):
    event_name = models.CharField(max_length=255, null=True)
    event_venue = models.CharField(max_length=255, null=True)
    event_type = models.CharField(max_length=255, blank=True, null=True)
    event_budget = models.IntegerField(null=True)
    event_guest_number = models.IntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    event_remote_arrange = models.CharField(max_length=255, blank=True, null=True)
    event_size = models.CharField(max_length=255, blank=True, null=True)
    event_description = models.CharField(max_length=2083, blank=True, null=True)
    event_client_name = models.CharField(max_length=255, blank=True, null=True)
    event_client = models.ForeignKey('client.Client', on_delete=models.CASCADE, blank=True, null=True)
    event_agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, blank=True, null=True)
    event_username = models.CharField(max_length=255, blank=True, null=True)
    is_secured = models.BooleanField(default=False)

    # stuff = models.ManyToManyField('agency.Staff')

    # on submit click on the  entry page, it redirects to the url below.
    def get_absolute_url(self):
        return reverse('event:index')
