from django.db import models


class Agent_Service(models.Model):
    agent = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_type = models.ForeignKey('vendor.Service_type', on_delete=models.CASCADE, default=None, blank=True, null=True)
    service_quantity = models.IntegerField;
    staff = models.ForeignKey('agency.Staff', on_delete=models.CASCADE, default=None, blank=True, null=True)


class Agent_Sponsor(models.Model):
    agent = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    sponsor = models.ForeignKey('sponsor.Sponsor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)
    sponsor_amount = models.IntegerField
    sponsor_pay_method = models.CharField(max_length=255)


class Event_Service(models.Model):
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    agent = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)

