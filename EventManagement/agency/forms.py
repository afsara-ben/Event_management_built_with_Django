from django import forms
from .models import *
from requestBrief.models import event_message


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ('agent_username', 'agent_email', 'agency_company_name', 'agency_company_website',
                  'agency_establish_time', 'agency_employee_number', 'agency_annual_turnover', 'agency_member_type',
                  'agency_description', 'agency_logo', 'agency_language', 'agency_contact_number', )


class AgencyInfoForm(forms.ModelForm):
    class Meta:
        model = Agency_Info
        fields = ('agency_company_address', 'agency_social_media', 'agency_service_provider', )


class AgencyBriefForm(forms.ModelForm):
    class Meta:
        model = AgencyBrief
        fields = ('agency_specialty', 'agency_interest', 'agency_remote_work', 'agency_event_budget',
                  'agency_company_name', )


class messageForm(forms.ModelForm):
    class Meta:
        model = event_message
        fields = ('email_subject', 'email_content', )

