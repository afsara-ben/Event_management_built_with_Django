from django.db import models
from datetime import datetime


class event_request(models.Model):
    service = models.CharField(max_length=2083, default=None, blank=True, null=True)
    range = models.CharField(max_length=2083, default=None, blank=True, null=True)
    location = models.CharField(max_length=2083, default=None, blank=True, null=True)
    language = models.CharField(max_length=2083, default=None, blank=True, null=True)
    goal = models.CharField(max_length=2083, default=None, blank=True, null=True)
    job = models.CharField(max_length=2083, default=None, blank=True, null=True)
    size = models.CharField(max_length=2083, default=None, blank=True, null=True)
    otherservice = models.CharField(max_length=2083, default=None, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    client_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    request_status = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    client_remote_work = models.CharField(max_length=255, default=None, blank=True, null=True)
    request_type = models.CharField(max_length=255, default=None, blank=True, null=True)


class event_message(models.Model):
    client_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    client_email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    agency_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    email_subject = models.CharField(max_length=255, default=None, blank=True, null=True)
    email_content = models.CharField(max_length=2083, default=None, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    agency_type = models.CharField(max_length=255, default=None, blank=True, null=True)

