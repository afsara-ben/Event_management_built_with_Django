from django.db import models


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=255)
    sponsor_email = models.CharField(max_length=255)
    sponsor_password = models.CharField(max_length=255)
    sponsor_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    sponsor_occupation = models.CharField(max_length=255, default=None, blank=True, null=True)
    sponsor_work_website = models.CharField(max_length=2083, default=None, blank=True, null=True)
    sponsor_company_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    sponsor_contact_number = models.IntegerField(default=None, blank=True, null=True)

