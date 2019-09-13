from datetime import datetime

from django.db import models


class AdminAgency_Transaction(models.Model):
    admin_agency_amount = models.IntegerField(default=None, blank=True, null=True)
    admin_agency_pay_method = models.CharField(max_length=255, default=None, blank=True, null=True)
    admin_agency_pay_status = models.CharField(max_length=255, default=None, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True, null=True)
    agent_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    agent_first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    agent_last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_country = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_address = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_postal_code = models.IntegerField(default=None, blank=True, null=True)
    agency_address_division = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency_vat_number = models.IntegerField(default=None, blank=True, null=True)
    agency_billing_email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    agency_status = models.CharField(max_length=20, default=None, blank=True, null=True)
    agency_card_number = models.IntegerField(default=None, blank=True, null=True)
    agency_cvv_number = models.IntegerField(default=None, blank=True, null=True)
    agency_card_year = models.IntegerField(default=None, blank=True, null=True)
    agency_card_month = models.CharField(max_length=255, default=None, blank=True, null=True)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)


class ClientAgency_Transaction(models.Model):
    client_agency_amount = models.IntegerField
    client_agency_date = models.DateField
    client_agency_time = models.TimeField
    client_agency_pay_method = models.CharField(max_length=255)
    client_agency_pay_status = models.CharField(max_length=255)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)


class ClientService_Transaction(models.Model):
    client_service_amount = models.IntegerField
    client_service_date = models.DateField
    client_service_time = models.TimeField
    client_service_pay_method = models.CharField(max_length=255)
    client_service_pay_status = models.CharField(max_length=255)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)

