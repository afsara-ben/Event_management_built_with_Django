from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor, Vendor_Info, VendorBrief
from .forms import VendorForm, VendorInfoForm, VendorBriefForm
from imageapp.models import Picture
from feedback.models import Feedback
from requestBrief.models import event_message
from transaction.models import AdminAgency_Transaction


def vendor_view(request):
    try:
        value = Vendor.objects.get(vendor_name=request.user.username)
    except Vendor.DoesNotExist:
        value = None
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=value)
        if form.is_valid():
            obj = form.save(commit=False)
            vendor_registration_username = request.user.username  # jishatech
            obj.vendor_name = vendor_registration_username
            obj.vendor_email = request.user.email
            obj.save()
            if obj.vendor_employee_number == None:
                obj.vendor_studio_size = "i do not care"
            elif obj.vendor_employee_number <= 10:
                obj.vendor_studio_size = "small studio"
            elif obj.vendor_employee_number <= 30:
                obj.vendor_studio_size = "medium studio"
            elif obj.vendor_employee_number <= 100:
                obj.vendor_studio_size = "big studio"
            elif obj.vendor_employee_number > 100:
                obj.vendor_studio_size = "group"
            else:
                obj.vendor_studio_size = "i do not care"
            obj.save()
            value = Vendor.objects.get(vendor_name=request.user.username)
        return render(request, 'vendor_form.html', {'form': form, 'value': value}, )
    else:
        form = VendorForm(instance=value)
    return render(request, 'vendor_form.html', {'form': form, 'value': value}, )


def vendor_success(request):
    value = Vendor.objects.filter(vendor_name=request.user.username).order_by('-id')[0]
    return render(request, 'vendor_post.html', {'value': value}, )


def edit_post(request):
    value = get_object_or_404(Vendor, vendor_name=request.user.username)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=value)

        if form.is_valid():
            obj = form.save(commit=False)
            vendor_registration_username = request.user.username  # jishatech
            obj.vendor_name = vendor_registration_username
            obj.vendor_email = request.user.email
            obj.save()
            if obj.vendor_employee_number <= 10:
                obj.vendor_studio_size = "small studio"
            elif obj.vendor_employee_number <= 30:
                obj.vendor_studio_size = "medium studio"
            elif obj.vendor_employee_number <= 100:
                obj.vendor_studio_size = "big studio"
            elif obj.vendor_employee_number > 100:
                obj.vendor_studio_size = "group"
            else:
                obj.vendor_studio_size = "i do not care"
            obj.save()
            return redirect('vendor_success')
    else:
        form = VendorForm(instance=value)
    return render(request, 'vendor_form.html', {'form': form, 'value': value}, )


def vendor_contact(request):
    if request.method == 'POST':
        form = VendorInfoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            vendor_registration_username = request.user.username  # jishatech
            vendor_registration_company = Vendor.objects.get(vendor_name=request.user.username)
            obj.vendor_name = vendor_registration_username
            obj.vendor_company_name = vendor_registration_company.vendor_company_name
            obj.save()
            # form.save()
            return redirect('vendor_contact_success')
    else:
        form = VendorInfoForm()
    return render(request, 'vendor_contact.html', {'form': form})


def vendor_contact_success(request):
    values = Vendor_Info.objects.all()
    return render(request, 'vendor_contact_post.html', {'values': values}, )


def preference_view(request):
    # try:
    #    value = AgencyBrief.objects.get(agent_username=request.user.username).order_by('id')
    #    return render(request, 'agency_form.html', {'value': value}, )
    # except AgencyBrief.DoesNotExist:
    #    value = None
    #logo = Picture.objects.filter(uploader=request.user.username, image_name="company_logo").order_by('date_added')[0]
    #designs = Picture.objects.filter(uploader=request.user.username).filter(~Q(image_name="company_logo")).all()
    vendor_company = Vendor.objects.get(vendor_name=request.user.username)
    reviews = Feedback.objects.filter(agency_name=vendor_company.vendor_company_name).all()
    requests = event_message.objects.all()
    payments = AdminAgency_Transaction.objects.all()
    if request.method == 'POST':
        form = VendorBriefForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            vendor_registration_username = request.user.username  # jishatech
            vendor_registration_company = Vendor.objects.get(vendor_name=request.user.username)
            obj.vendor_name = vendor_registration_username
            obj.vendor_company_name = vendor_registration_company.vendor_company_name
            obj.save()
            return redirect('vendor_preference_success')
    else:
        form = VendorBriefForm()
    return render(request, 'vendor_preference.html', {'form': form, 'vendor_company': vendor_company,
                                                      'reviews': reviews, 'requests': requests, 'payments': payments}, )


def preference_success(request):
    value = VendorBrief.objects.filter(vendor_name=request.user.username).order_by('-id')
    return render(request, 'vendor_preference_success.html', {'value': value}, )

