from django.db import models
from datetime import datetime
from django.db.models import Q
from django.urls import reverse


class AgencyQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(agency_company_name__icontains=query) |
                         Q(agency_company_website__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class AgencyManager(models.Manager):
    def get_queryset(self):
        return AgencyQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Agency(models.Model):
    agent_username = models.CharField(max_length=255, unique=True, default="", blank=True, null=True)
    agent_email = models.EmailField(max_length=255, default="", blank=True, null=True)
    agency_company_name = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_company_website = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_establish_time = models.IntegerField(default="", blank=True, null=True)
    agency_employee_number = models.IntegerField(default="", blank=True, null=True)
    agency_annual_turnover = models.IntegerField(default="", blank=True, null=True)
    agency_member_type = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_description = models.CharField(max_length=2083, default="", blank=True, null=True)
    agency_logo = models.ImageField(upload_to='images/', default="", blank=True, null=True)
    agency_language = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_contact_number = models.IntegerField(default="", blank=True, null=True)
    agency_studio_size = models.CharField(max_length=255, default=None, blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    agency_past_work = models.CharField(max_length=255, default="", blank=True, null=True)

    objects = AgencyManager()


class AgencyInfoQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(agency_company_name__icontains=query) |
                         Q(agency_company_address__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class AgencyInfoManager(models.Manager):
    def get_queryset(self):
        return AgencyInfoQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Agency_Info(models.Model):
    agency_company_name = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_company_address = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_service_provider = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_social_media = models.CharField(max_length=2083, default=None, blank=True, null=True)
    agency_past_work = models.CharField(max_length=2083, default="", blank=True, null=True)
    agency_upcoming_work = models.CharField(max_length=2083, default="", blank=True, null=True)
    agency_provide_design = models.CharField(max_length=2083, default="", blank=True, null=True)
    agent_username = models.CharField(max_length=255, default="")
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    objects = AgencyInfoManager()

#    def get_absolute_url(self):
#        return reverse('popup', kwargs={'agency_company_name': self.agency_company_name})


class AgencyBriefQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(agency_company_name__icontains=query) |
                         Q(agency_interest__icontains=query) |
                         Q(agency_specialty__icontains=query) |
                         (Q(agency_budget_upper__gte=query) &
                         Q(agency_budget_lower__lte=query))
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class AgencyBriefManager(models.Manager):
    def get_queryset(self):
        return AgencyBriefQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class AgencyBrief(models.Model):
    agency_company_name = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_specialty = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_interest = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_remote_work = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_event_budget = models.CharField(max_length=255, default="", blank=True, null=True)
    agency_budget_upper = models.IntegerField(default=None, blank=True, null=True)
    agency_budget_lower = models.IntegerField(default=None, blank=True, null=True)
    agent_username = models.CharField(max_length=255, default="")
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    objects = AgencyBriefManager()


class Staff(models.Model):
    staff_name = models.CharField(max_length=255)
    staff_designation = models.CharField(max_length=255)
    staff_email = models.CharField(max_length=255)
    staff_contact_number = models.IntegerField
    agent_username = models.CharField(max_length=255, default=None)
    # agency_company = models.ForeignKey('Agency', on_delete=models.CASCADE)

