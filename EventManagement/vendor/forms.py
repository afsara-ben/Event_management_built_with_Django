from django import forms
from .models import *


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('vendor_name', 'vendor_email', 'vendor_company_name', 'vendor_company_website',
                  'vendor_establish_time', 'vendor_employee_number', 'vendor_annual_turnover', 'vendor_member_type',
                  'vendor_description', 'vendor_language', 'vendor_contact_number', )


class VendorInfoForm(forms.ModelForm):
    class Meta:
        model = Vendor_Info
        fields = ('vendor_company_address', 'vendor_social_media', )


class VendorBriefForm(forms.ModelForm):
    class Meta:
        model = VendorBrief
        fields = ('vendor_service', 'vendor_specialty', 'vendor_interest', 'vendor_remote_work', 'vendor_event_budget',
                  'vendor_company_name', )

