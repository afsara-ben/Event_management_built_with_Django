from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    client_password = models.CharField(max_length=255)
    client_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    client_occupation = models.CharField(max_length=255, default=None, blank=True, null=True)
    client_work_website = models.CharField(max_length=2083, default=None, blank=True, null=True)
    client_company_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    client_contact_number = models.IntegerField(default=None, blank=True, null=True)

