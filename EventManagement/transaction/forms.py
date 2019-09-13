from django import forms
from .models import *


class AgencyTransactionForm(forms.ModelForm):
    class Meta:
        model = AdminAgency_Transaction
        fields = ('agent_first_name', 'agent_last_name', 'agency_name', 'agency_country', 'agency_address',
                  'agency_postal_code', 'agency_address_division', 'agency_vat_number', 'agency_billing_email',
                  'agency_card_number', 'agency_cvv_number', 'agency_card_year', 'agency_card_month', 'date_added',
                  'agent_name', )

