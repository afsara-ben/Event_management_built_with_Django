from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from reg_group.models import User, User_Info


def feedback_form(request):
    global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            client_registration_username = request.user.username  # jishatech
            obj.customer_name = client_registration_username
            obj.customer_email = request.user.email
            obj.agency_name = sku
            reviewer_type = User.objects.get(username=request.user.username)
            if reviewer_type.is_agency == 1:
                print(sku)
                obj.save()
                obj.overall = (obj.is_favorite+obj.behaviour+obj.price_fairness+obj.professionalism)/4
                obj.save()
                # form.save()
                return render(request, 'agency_rate_client.html', {'obj': obj})
            elif reviewer_type.is_vendor == 1:
                print(sku)
                obj.save()
                obj.overall = (obj.is_favorite+obj.behaviour+obj.price_fairness+obj.professionalism)/4
                obj.save()
                # form.save()
                return render(request, 'thanks.html', {'obj': obj})
            else:
                print(sku)
                obj.save()
                obj.overall = (obj.is_favorite+obj.behaviour+obj.price_fairness+obj.professionalism)/4
                obj.save()
                # form.save()
                return render(request, 'thanks.html', {'obj': obj})
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def service_feedback_form(request):
    global sku
    if request.method == 'GET':
        sku = request.GET.get('sku')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            client_registration_username = request.user.username  # jishatech
            obj.customer_name = client_registration_username
            obj.customer_email = request.user.email
            obj.agency_name = sku
            print(sku)
            obj.save()
            # form.save()
            return render(request, 'servicethanks.html', {'obj': obj})
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})


def feedback_view(request):
    values = Feedback.objects.all()
    obj = Feedback.objects.filter(agency_name=sku).order_by('date_added')[0]
    return render(request, '/client/mymatch/agency/?sku='+obj.agency_name, {'values': values})

