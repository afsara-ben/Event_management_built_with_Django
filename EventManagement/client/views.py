from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, _get_queryset
from .forms import Clientform
from .models import Client


def client_view(request):
    try:
        value = Client.objects.get(client_name=request.user.username)
    except Client.DoesNotExist:
        value = Client()
        value.client_name=request.user.username
        value.client_email=request.user.email
        value.save()
    if request.method == 'POST' :
        form = Clientform(request.POST,instance=value)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            # value = Client.objects.get(client_name=request.user.username)
        return render(request, 'client_form.html', {'form': form, 'value': value}, )
    else:
        form = Clientform(instance=value)
    return render(request, 'client_form.html', {'form': form, 'value': value}, )

