from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_agency:
            return redirect('agency:agency_profile')
        elif request.user.is_client:
            return redirect('client:client_profile')
        else:
            return redirect('vendor:vendor_profile')
    return render(request, 'home.html')

