from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset
from .forms import AgencyForm, AgencyInfoForm, AgencyBriefForm, messageForm
from .models import Agency, Agency_Info, AgencyBrief
from imageapp.models import Picture
from feedback.models import Feedback
from requestBrief.models import event_message
from transaction.models import AdminAgency_Transaction
from vendor.models import *
from reg_group.models import User, User_Info
from event.models import Event


def preference_view(request):
    # try:
    #    value = AgencyBrief.objects.get(agent_username=request.user.username).order_by('id')
    #    return render(request, 'agency_form.html', {'value': value}, )
    # except AgencyBrief.DoesNotExist:
    #    value = None
    logo = Picture.objects.filter(uploader=request.user.username, image_name="company_logo").order_by('date_added')[0]
    designs = Picture.objects.filter(uploader=request.user.username).filter(~Q(image_name="company_logo")).all()
    agency_company = Agency.objects.get(agent_username=request.user.username)
    reviews = Feedback.objects.filter(agency_name=agency_company.agency_company_name).all()
    requests = event_message.objects.all()
    payments = AdminAgency_Transaction.objects.all()
    works = Agency_Info.objects.filter(agency_company_name=agency_company.agency_company_name)

    if request.method == 'POST':
        form = AgencyBriefForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.agent_username = agency_registration_username
            obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            return redirect('agency_preference_success')
    else:
        form = AgencyBriefForm()
    return render(request, 'agency_preference.html', {'form': form, 'logo': logo, 'designs': designs,
                                                      'reviews': reviews, 'requests': requests, 'payments': payments,
                                                      'works': works}, )


def event_request_event(request):
    posts = event_message.objects.all()
    return render(request, 'agency_preference.html', {'posts': posts})


def preference_success(request):
    value = AgencyBrief.objects.filter(agent_username=request.user.username).order_by('-id')
    return render(request, 'agency_preference_success.html', {'value': value}, )


def agency_view(request):
    try:
        value = Agency.objects.get(agent_username=request.user.username)
        logo = Picture.objects.filter(uploader=request.user.username, image_name="company_logo").order_by('date_added')[
            0]
        design = Picture.objects.filter(uploader=request.user.username).filter(~Q(image_name="company_logo")).all()
        return render(request, 'agency_form.html', {'value': value, 'logo': logo, 'design': design}, )
    except Agency.DoesNotExist:
        value = None
        if request.method == 'POST':
            form = AgencyForm(request.POST, instance=value)

            if form.is_valid():
                obj = form.save(commit=False)
                agency_registration_username = request.user.username  # jishatech
                obj.agent_username = agency_registration_username
                obj.agent_email = request.user.email
                obj.save()
                if obj.agency_employee_number <= 10:
                    obj.agency_studio_size = "small studio"
                elif obj.agency_employee_number <= 30:
                    obj.agency_studio_size = "medium studio"
                elif obj.agency_employee_number <= 100:
                    obj.agency_studio_size = "big studio"
                elif obj.agency_employee_number > 100:
                    obj.agency_studio_size = "group"
                else:
                    obj.agency_studio_size = "i do not care"
                obj.save()
                return redirect('agency_success')
        else:
            form = AgencyForm(instance=value)
        return render(request, 'agency_form.html', {'form': form, 'value': value, 'logo': logo, 'design': design}, )


def agency_contact(request):
    if request.method == 'POST':
        form = AgencyInfoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.agent_username = agency_registration_username
            obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('agency_contact_success')
    else:
        form = AgencyInfoForm()
    return render(request, 'agency_contact.html', {'form': form})


def agency_success(request):
    value = Agency.objects.filter(agent_username=request.user.username).order_by('-id')[0]
    return render(request, 'agency_post.html', {'value': value}, )


def agency_contact_success(request):
    values = Agency_Info.objects.all()
    return render(request, 'agency_contact_post.html', {'values': values}, )


def edit_post(request):
    value = get_object_or_404(Agency, agent_username=request.user.username)
    if request.method == 'POST':
        form = AgencyForm(request.POST, instance=value)

        if form.is_valid():
            #  form = Agency.objects.get(agent_username=request.user.username)
            #  form.agency_company_name = request.POST['agency_company_name']
            # Agency.objects.filter(agent_username=request.user.username).update(
            # agency_company_name=request.POST['agency_company_name'],)
            # Agency.objects.filter(agent_username=request.user.username).update(
            # agency_company_website=request.POST['agency_company_website'],)
            #  form.save()
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            obj.agent_username = agency_registration_username
            obj.agent_email = request.user.email
            obj.save()
            if obj.agency_employee_number <= 10:
                obj.agency_studio_size = "small studio"
            elif obj.agency_employee_number <= 30:
                obj.agency_studio_size = "medium studio"
            elif obj.agency_employee_number <= 100:
                obj.agency_studio_size = "big studio"
            elif obj.agency_employee_number > 100:
                obj.agency_studio_size = "group"
            else:
                obj.agency_studio_size = "i do not care"
            obj.save()
            return redirect('agency_success')
    else:
        form = AgencyForm(instance=value)
    return render(request, 'agency_form.html', {'form': form, 'value': value}, )


def edit_post_contact(request):
    values = get_object_or_404(Agency_Info, agent_username=request.user.username)
    if request.method == 'POST':
        form = AgencyInfoForm(request.POST, instance=values)

        if form.is_valid():
            form = Agency_Info.objects.get(agent_username=request.user.username)
            print(request.POST.get('id'))
            form.agency_company_address = request.POST.get('agency_company_address', False)
            form.save()
            return redirect('agency_contact_success')
    else:
        form = AgencyInfoForm(instance=values)
    return render(request, 'agency_contact.html', {'form': form, 'values': values}, )


def agency_vendor_success(request):
    # global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
        values = Agency_Info.objects.filter(agent_username=request.user.username).filter(agency_service_provider=sku)
        service = Vendor.objects.filter(vendor_company_name=sku).order_by('date_added')[0]
        service_info = Vendor_Info.objects.filter(vendor_company_name=sku).all()
        if sku:
            context = {
                'sku': sku,
                'values': values,
                'service': service,
                'service_info': service_info,
            }
            return render(request, 'agency_vendor_match.html', context)


def agency_message(request):
    # value = event_request.objects.latest('date_added')
    # posts = event_request.objects.filter(client_name=request.user.username).order_by('date_added')[0]
    # client_detail = User.objects.filter(username=posts.client_name).order_by('id')[0]
    global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
    if request.method == 'POST':
        form = messageForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_detail = User.objects.get(username=sku)
            client_registration_username = request.user.username  # jishatech
            obj.client_name = client_registration_username
            obj.client_email = request.user.email
            obj.agency_name = sku
            obj.agency_email = agency_detail.email
            obj.agency_type = "agencyclient"
            obj.save()
            # form.save()
            return render(request, 'agency_reply_message.html', {'obj': obj})
    else:
        form = messageForm()
    # clientInfo = event_message.objects.filter(agency_name=sku).order_by('date_added')[0]
    return render(request, 'agency_reply_message.html', {'form': form, 'sku': sku})


def clientlist_view(request):
    clients = Event.objects.filter(event_username=request.user.username)
    review_client = Event.objects.filter(event_username=request.user.username).order_by('id')[0]
    feedback = Feedback.objects.filter(agency_name=review_client.event_client_name).all()
    return render(request, 'clientlist.html', {'clients': clients, 'feedback': feedback})


def agencylist_view(request):
    agency_list_view = Agency.objects.all()
    agency_info = Agency_Info.objects.all()
    agency_brief = AgencyBrief.objects.all()
    feedback = Feedback.objects.all()
    return render(request, 'agency_list_view.html', {'agencylist': agency_list_view, 'feedback': feedback,
                                                     'agencyinfo': agency_info, 'agencybrief': agency_brief})
