from itertools import chain

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from products.views import index
# from profile.models import user
from requestBrief.forms import requestForm, messageForm, servicerequestForm
from requestBrief.models import event_request
from agency.models import AgencyBrief, Agency_Info, Agency
from vendor.models import VendorBrief, Vendor_Info, Vendor
from reg_group.models import User
from imageapp.models import Picture
from imageapp.forms import ImageForm
from imageapp.views import logo_success
from feedback.models import Feedback
from requestBrief.models import event_message

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required


def request_view(request):
    client_message = event_message.objects.all()
    requests = event_request.objects.all()
    form_class = requestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = requestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        obj.client_name = request.user.username
        obj.request_type = 'agency'
        obj.request_status = 'pending'
        print(service)
        obj.save()
        #    return redirect('createBrief')
        return redirect('mymatch')

    else:
        form = requestForm()
    return render(request, 'popup.html', {'form': form, 'client_message': client_message, 'requests': requests}, )


def request_success(request):
    form_class = requestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = requestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        print(service)
        obj.client_name = request.user.username
        obj.request_status = 'pending'
        obj.save()
        #    return redirect('createBrief')
        return redirect('mymatch')

    value = event_request.objects.latest('date_added')
    return render(request, 'popup.html', {'value': value}, )


def popup(request):
    brief = event_request.objects.all()
    context = {'brief': brief}
    # my_user = user.objects.all()
    #    return render(request, 'eventDashBoard.html', {'brief': user})
    return render(request, 'popup.html', context)


def home(request):
    return render(request, 'home.html')


def match(request):
    client_message = event_message.objects.all()
    requests = event_request.objects.all()
    count = 70
    value = event_request.objects.latest('date_added')
    agency_brief_match = AgencyBrief.objects.filter((Q(agency_specialty__icontains=value.service) |
                                                     Q(agency_interest__icontains=value.service)) &
                                                    Q(agency_remote_work__icontains=value.client_remote_work) &
                                                    Q(agency_event_budget__icontains=value.range)).distinct()

    if value.client_remote_work is "no":
        agency_info_match = Agency_Info.objects.filter(Q(agency_company_address__icontains=value.location)).distinct()
    else:
        agency_info_match = Agency_Info.objects.filter(Q(agency_company_address__icontains=value.location) |
                                                       ~Q(agency_company_address__icontains=value.location)).distinct()

    if value.size != "I do not care":
        agency_match = Agency.objects.filter(Q(agency_language__icontains=value.language) &
                                             Q(agency_studio_size__icontains=value.size)).distinct()

    else:
        agency_match = Agency.objects.filter(Q(agency_language__icontains=value.language)).distinct()

    result_list_list = sorted(chain(agency_brief_match,
                                    agency_match,
                                    agency_info_match,
                                    ),
                              key=lambda instance: instance.date_added)
    result_list = list(set(result_list_list))

    sku = result_list

    feedback = Feedback.objects.filter(agency_name=request.user.username)
    print(request.user.username)

    context = {
        'client_message': client_message,
        'requests': requests,
        'value': value,
        'result_list': result_list,
        'count': count,
        'agency_brief_match': agency_brief_match,
        'agency_match': agency_match,
        'agency_info_match': agency_info_match,
        'sku': sku,
        'feedback' : feedback,
    }
    return render(request, 'popup.html', context, )


def match_success(request):
    value = event_request.objects.latest('date_added')
    if request.method == 'GET':
        sku = request.GET.get('sku')
        if not sku:
            return render(request, 'popup.html')
        else:
            message = "Agency criteria matched"
            agency_detail = Agency.objects.get(agency_company_name=sku)
            agency_info_detail = Agency_Info.objects.filter(agency_company_name=sku).order_by('date_added')[0]
            agency_info_address = Agency_Info.objects.filter(agency_company_name=sku)
            agency_brief_detail = AgencyBrief.objects.filter(agency_company_name=sku).order_by('date_added')[0]
            posts = Picture.objects.filter(uploader=agency_detail.agent_username).order_by('date_added')
            feedback_review = Feedback.objects.filter(agency_name=sku).all()
            service_match = "Service criteria matched" if value.service.lower() in agency_brief_detail.agency_specialty.lower() or agency_brief_detail.agency_interest.lower() else ""
            language_match = "Language criteria matched" if agency_detail.agency_language.lower() == value.language.lower() else ""
            size_match = "Agency size criteria matched" if agency_detail.agency_studio_size.lower() == value.size.lower() else ""
            location_match = "Agency location criteria matched" if value.location.lower() in agency_info_detail.agency_company_address.lower() else ""
            budget_match = "Agency budget criteria method" if agency_brief_detail.agency_event_budget.lower() == value.range.lower() else ""
            context = {
                'sku': sku,
                'message': message,
                'agency_detail': agency_detail,
                'agency_info_detail': agency_info_detail,
                'agency_brief_detail': agency_brief_detail,
                'agency_info_address': agency_info_address,
                'posts': posts,
                'value': value,
                'service_match': service_match,
                'language_match': language_match,
                'size_match': size_match,
                'location_match': location_match,
                'budget_match': budget_match,
                'feedback_review': feedback_review,
            }
            return render(request, 'agency_match.html', context)


# def client_sends_message(request):
#     # value = event_request.objects.latest('date_added')
#     # posts = event_request.objects.filter(client_name=request.user.username).order_by('date_added')[0]
#     # client_detail = User.objects.filter(username=posts.client_name).order_by('id')[0]
#     global sku
#     if request.method == 'GET':
#         sku = request.GET.get('sku')
#     if request.method == 'POST':
#         form = messageForm(request.POST)
#
#         if form.is_valid():
#             obj = form.save(commit=False)
#             client_detail = User.objects.get(username=sku)
#             client_registration_username = request.user.username  # jishatech
#             obj.client_name = client_registration_username
#             obj.client_email = request.user.email
#             obj.agency_name = sku
#             obj.client_email = client_detail.email
#             obj.agency_type = "agency"
#             obj.save()
#             # form.save()
#             return render(request, 'agency_message.html', {'obj': obj})
#     else:
#         form = messageForm()
#     # clientInfo = event_message.objects.filter(agency_name=sku).order_by('date_added')[0]
#     return render(request, 'agency_message.html', {'form': form, 'sku': sku})

def client_request_history(request):
    posts = event_request.objects.filter(client_name=request.user.username).all()

    send_mail('Subject here', 'Here is the message. Send. Done.', 'jsultanajisha@gmail.com',
              ['jsultanajisha@gmail.com'], fail_silently=False, )
    # for value in values:
    #    print(value.service)
    context = {
        'posts': posts,
    }
    return render(request, 'popup.html', context, )


def match_message(request):
    value = event_request.objects.latest('date_added')
    posts = event_request.objects.filter(client_name=request.user.username).order_by('date_added')[0]
    client_detail = User.objects.filter(username=posts.client_name).order_by('id')[0]
    global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
    if request.method == 'POST':
        form = messageForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            client_registration_username = request.user.username  # jishatech
            obj.client_name = client_registration_username
            obj.client_email = request.user.email
            obj.agency_name = sku

            print(obj.agency_name)
            agency_detail = Agency.objects.get(agency_company_name=sku)
            obj.agency_email = agency_detail.agent_email
            obj.agency_type = "agency"
            obj.save()
            # form.save()
            return render(request, 'agency_message.html', {'obj': obj})
    else:
        form = messageForm()
    agencyName = event_message.objects.filter(agency_name=sku)
    return render(request, 'agency_message.html', {'form': form, 'value': value, 'posts': posts,
                                                   'client_detail': client_detail, 'sku': sku}
                  )


def agencyclient_message(request):
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
            return render(request, 'agencyclient_message.html', {'obj': obj})
    else:
        form = messageForm()
    # clientInfo = event_message.objects.filter(agency_name=sku).order_by('date_added')[0]
    return render(request, 'agencyclient_message.html', {'form': form, 'sku': sku})

def servicerequest_view(request):
    client_message = event_message.objects.all()
    requests = event_request.objects.all()
    form_class = servicerequestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = servicerequestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        obj.client_name = request.user.username
        obj.request_type = 'vendor'
        obj.request_status = 'pending'
        print(service)
        obj.save()
        #    return redirect('createBrief')
        return redirect('myservicematch')

    else:
        form = servicerequestForm()
    return render(request, 'servicepopup.html', {'form': form, 'client_message': client_message,'requests': requests}, )


def servicerequest_success(request):
    form_class = servicerequestForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = servicerequestForm(request.POST)

    if form.is_valid():
        obj = form.save(commit=False)
        service = request.POST.getlist('service')
        # obj.service = service
        print(service)
        obj.client_name = request.user.username
        obj.request_status = 'pending'
        obj.save()
        #    return redirect('createBrief')
        return redirect('myservicematch')

    value = event_request.objects.latest('date_added')
    return render(request, 'servicepopup.html', {'value': value}, )


def servicematch(request):
    client_message = event_message.objects.all()
    requests = event_request.objects.all()
    count = 70
    value = event_request.objects.latest('date_added')
    vendor_brief_match = VendorBrief.objects.filter(Q(vendor_service__icontains=value.otherservice) &
                                                    (Q(vendor_specialty__icontains=value.service) |
                                                     Q(vendor_interest__icontains=value.service)) &
                                                    Q(vendor_remote_work__icontains=value.client_remote_work) &
                                                    Q(vendor_event_budget__icontains=value.range))

    if value.client_remote_work is "no":
        vendor_info_match = Vendor_Info.objects.filter(Q(vendor_company_address__icontains=value.location)).distinct()
    else:
        vendor_info_match = Vendor_Info.objects.filter(Q(vendor_company_address__icontains=value.location) |
                                                       ~Q(vendor_company_address__icontains=value.location)).distinct()

    if value.size != "I do not care":
        vendor_match = Vendor.objects.filter(Q(vendor_language__icontains=value.language) &
                                             Q(vendor_studio_size__icontains=value.size)).distinct()

    else:
        vendor_match = Vendor.objects.filter(Q(vendor_language__icontains=value.language)).distinct()

    result_list_list = sorted(chain(vendor_brief_match,
                                    vendor_match,
                                    vendor_info_match,
                                    ),
                              key=lambda instance: instance.date_added)
    result_list = list(set(result_list_list))

    sku = result_list

    context = {
        'client_message' : client_message,
        'requests' : requests,
        'value': value,
        'result_list': result_list,
        'count': count,
        'vendor_brief_match': vendor_brief_match,
        'vendor_match': vendor_match,
        'vendor_info_match': vendor_info_match,
        'sku': sku,
    }
    return render(request, 'servicepopup.html', context, )

def servicematch_success_showlittle(request):
    value = event_request.objects.latest('date_added')
    sku="jishaserviceprovider"
    print ("here1")
    if request.method == 'GET':
        # sku = request.GET.get('jishaserviceprovider')
        print ("here2")
        if not sku:
            print ("here3")
            return render(request, 'servicepopup.html')
        else:
            print ("here4")
            message = "Vendor criteria matched"
            vendor_detail = Vendor.objects.get(vendor_company_name=sku)
            vendor_info_detail = Vendor_Info.objects.filter(vendor_company_name=sku).order_by('date_added')[0]
            vendor_info_address = Vendor_Info.objects.filter(vendor_company_name="sku")
            vendor_brief_detail = VendorBrief.objects.filter(vendor_company_name=sku).order_by('date_added')[0]
            posts = Picture.objects.filter(uploader=vendor_detail.vendor_name).order_by('date_added')
            feedback_review = Feedback.objects.filter(agency_name=sku).all()
            service_match = "Service criteria matched" if value.service.lower() in vendor_brief_detail.vendor_specialty.lower() or vendor_brief_detail.vendor_interest.lower() else ""
            language_match = "Language criteria matched" if vendor_detail.vendor_language.lower() == value.language.lower() else ""
            size_match = "Agency size criteria matched" if vendor_detail.vendor_studio_size.lower() == value.size.lower() else ""
            location_match = "Agency location criteria matched" if value.location.lower() in vendor_info_detail.vendor_company_address.lower() else ""
            budget_match = "Agency budget criteria method" if vendor_brief_detail.vendor_event_budget.lower() == value.range.lower() else ""
            context = {
                'sku': sku,
                'message': message,
                'vendor_detail': vendor_detail,
                'vendor_info_detail': vendor_info_detail,
                'vendor_brief_detail': vendor_brief_detail,
                'vendor_info_address': vendor_info_address,
                'posts': posts,
                'value': value,
                'service_match': service_match,
                'language_match': language_match,
                'size_match': size_match,
                'location_match': location_match,
                'budget_match': budget_match,
                'feedback_review': feedback_review,
            }
            print ("here5")
            return render(request, 'servicepopup.html', context)


def servicematch_success(request):
    value = event_request.objects.latest('date_added')
    if request.method == 'GET':
        sku = request.GET.get('sku')
        if not sku:
            return render(request, 'servicepopup.html')
        else:
            message = "Vendor criteria matched"
            vendor_detail = Vendor.objects.get(vendor_company_name=sku)
            vendor_info_detail = Vendor_Info.objects.filter(vendor_company_name=sku).order_by('date_added')[0]
            vendor_info_address = Vendor_Info.objects.filter(vendor_company_name=sku)
            vendor_brief_detail = VendorBrief.objects.filter(vendor_company_name=sku).order_by('date_added')[0]
            posts = Picture.objects.filter(uploader=vendor_detail.vendor_name).order_by('date_added')
            feedback_review = Feedback.objects.filter(agency_name=sku).all()
            service_match = "Service criteria matched" if value.service.lower() in vendor_brief_detail.vendor_specialty.lower() or vendor_brief_detail.vendor_interest.lower() else ""
            language_match = "Language criteria matched" if vendor_detail.vendor_language.lower() == value.language.lower() else ""
            size_match = "Agency size criteria matched" if vendor_detail.vendor_studio_size.lower() == value.size.lower() else ""
            location_match = "Agency location criteria matched" if value.location.lower() in vendor_info_detail.vendor_company_address.lower() else ""
            budget_match = "Agency budget criteria method" if vendor_brief_detail.vendor_event_budget.lower() == value.range.lower() else ""
            context = {
                'sku': sku,
                'message': message,
                'vendor_detail': vendor_detail,
                'vendor_info_detail': vendor_info_detail,
                'vendor_brief_detail': vendor_brief_detail,
                'vendor_info_address': vendor_info_address,
                'posts': posts,
                'value': value,
                'service_match': service_match,
                'language_match': language_match,
                'size_match': size_match,
                'location_match': location_match,
                'budget_match': budget_match,
                'feedback_review': feedback_review,
            }
            return render(request, 'vendor_match.html', context)


def servicematch_message(request):
    value = event_request.objects.latest('date_added')
    posts = event_request.objects.filter(client_name=request.user.username).order_by('date_added')[0]
    client_detail = User.objects.filter(username=posts.client_name).order_by('id')[0]
    global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
    if request.method == 'POST':
        form = messageForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            client_registration_username = request.user.username  # jishatech
            obj.client_name = client_registration_username
            obj.client_email = request.user.email
            obj.agency_name = sku
            vendor_detail = Vendor.objects.get(vendor_company_name=sku)
            obj.agency_email = vendor_detail.vendor_email
            obj.agency_type = "vendor"
            obj.save()
            # form.save()
            return render(request, 'vendor_message.html', {'obj': obj})
    else:
        form = messageForm()
    # vendorName = event_message.objects.filter(agency_name=sku).order_by('date_added')[0]
    return render(request, 'vendor_message.html', {'form': form, 'value': value, 'posts': posts,
                                                   'client_detail': client_detail, 'sku': sku}
                  )

