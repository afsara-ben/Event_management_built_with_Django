from django.db import models


class SponsorAgency_Delivery(models.Model):
    sponsor_agency_amount = models.IntegerField
    sponsor_agency_date = models.DateField
    sponsor_agency_time = models.TimeField
    sponsor_agency_pay_method = models.CharField(max_length=255)
    sponsor_agency_pay_status = models.CharField(max_length=255)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    sponsor = models.ForeignKey('sponsor.Sponsor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)


class VendorAgency_Delivery(models.Model):
    vendor_agency_amount = models.IntegerField
    vendor_agency_date = models.DateField
    vendor_agency_time = models.TimeField
    vendor_agency_quantity = models.IntegerField
    vendor_agency_pay_method = models.CharField(max_length=255)
    vendor_agency_pay_status = models.CharField(max_length=255)
    agency = models.ForeignKey('agency.Agency', on_delete=models.CASCADE, default=None, blank=True, null=True)
    vendor = models.ForeignKey('vendor.Vendor', on_delete=models.CASCADE, default=None, blank=True, null=True)
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE, default=None, blank=True, null=True)
    vendor_type = models.ForeignKey('vendor.Service_type', on_delete=models.CASCADE, default=None, blank=True, null=True)

