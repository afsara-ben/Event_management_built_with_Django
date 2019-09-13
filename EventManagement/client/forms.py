from django import forms
from .models import *

class Clientform(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'client_email', 'client_address', 'client_occupation',
                  'client_work_website', 'client_company_name', 'client_contact_number', )