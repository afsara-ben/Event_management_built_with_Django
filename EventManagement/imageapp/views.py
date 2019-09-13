from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from agency.models import Agency


# Create your views here.
def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.uploader = agency_registration_username
            obj.image_name = "company_logo"
            # obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('agency_preference')
    else:
        form = ImageForm()
    return render(request, 'image_form.html', {'form': form})


def vendor_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.uploader = agency_registration_username
            obj.image_name = "company_logo"
            # obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('vendor_upload')
    else:
        form = ImageForm()
    return render(request, 'image_form.html', {'form': form})


def success(request):
    posts = Picture.objects.filter(uploader=request.user.username).order_by('date_added')[0]
    return render(request, 'agency_preference.html', {'posts': posts})
    # return HttpResponse('successfuly uploaded')


def logo_success(request):
    agency = Agency.objects.filter(agent_username=request.user.username)
    posts = Picture.objects.filter(uploader=agency.agent_username).filter(image_name="company_logo")
    return render(request, 'agency_match.html', {'posts': posts})
    #return HttpResponse('successfuly uploaded')


def design_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.uploader = agency_registration_username
            # obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('agency_preference')
    else:
        form = ImageForm()
    return render(request, 'design_form.html', {'form': form})


def vendor_design_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            obj.uploader = agency_registration_username
            # obj.agency_company_name = agency_registration_company.agency_company_name
            obj.save()
            # form.save()
            return redirect('vendor_preference')
    else:
        form = ImageForm()
    return render(request, 'design_form.html', {'form': form})


def design_work(request):
    agency = Agency.objects.filter(agent_username=request.user.username)
    posts = Picture.objects.filter(uploader=agency.agent_username).filter(~Q(image_name="company_logo"))
    return render(request, 'agency_match', {'posts': posts})

