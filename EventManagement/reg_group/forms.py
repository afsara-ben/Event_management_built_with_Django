from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from reg_group.models import User
from imageapp.models import Picture
from imageapp.forms import ImageForm
from agency.models import *
from agency.forms import *


class AgencySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agency = True
        if commit:
            user.save()
            form = ImageForm().save(commit=False)
            agency_registration_username = user.username  # jishatech
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            form.uploader = agency_registration_username
            form.image_name = "company_logo"
            form.image_file = "images/phineas.jpg"
            # obj.agency_company_name = agency_registration_company.agency_company_name
            form.save()
            obj = AgencyForm().save(commit=False)
            obj.agent_username = user.username
            obj.agent_email = user.email
            obj.agency_company_name = ""
            obj.agency_company_website = ""
            obj.agency_establish_time = 0
            obj.agency_employee_number = 0
            obj.agency_annual_turnover = 0
            obj.agency_member_type = ""
            obj.agency_description = ""
            obj.agency_logo = "images/phineas.jpg"
            obj.agency_language = ""
            obj.agency_contact_number = 0
            obj.save()
        return user


class ClientSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        #if commit:
        user.save()
        return user


class VendorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        #if commit:
        user.save()
        return user

