from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgencyTransactionForm
from .models import AdminAgency_Transaction
from agency.models import Agency


def payment_view(request):
    if request.method == 'POST':
        form = AgencyTransactionForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            agency_registration_username = request.user.username  # jishatech
            obj.agent_name = agency_registration_username
            # agency_registration_company = Agency.objects.get(agent_username=request.user.username)
            # obj.agency_name = agency_registration_company.agency_company_name
            obj.agency_vat_number = 15
            obj.admin_agency_pay_method = "credit card"
            obj.admin_agency_amount = 15000
            obj.save()
            obj.admin_agency_pay_status = "paid"
            obj.agency_status = "verified"
            obj.save()
            return redirect('agency_payment_success')
    else:
        form = AgencyTransactionForm()
    return render(request, 'agency_payment.html', {'form': form})


def payment_success(request):
    value = AdminAgency_Transaction.objects.filter(agent_name=request.user.username).order_by('-date_added')[0]
    return render(request, 'agency_payment_success.html', {'value': value})

