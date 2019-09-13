from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.urls import reverse


from tickets.models import Ticket
from .forms import TicketForm


def ViewTicket(request):
    ticket_list = Ticket.objects.all()

    return render(request, 'ticket/bookTicket.html', {'ticket_list': ticket_list})


def TicketEntry(request):
    # print("here")
    if request.method == 'POST':
    #
    #     print("here")
    #     if request.POST.get('ticket_for_event'):
    #         post = Ticket()
    #         post.ticket_for_event = request.POST.get('ticket_for_event')
    #         post.save()
    #
    #         return render(request, 'ticket/bookTicket.html')
    #
    #     else:
    #         form=
    #         return render(request, 'ticket/bookTicket.html')

        form = TicketForm(request.POST or None)
        print("posted")
        if form.is_valid():
            print("form valid")
            obj = form.save(commit=False)
            client_registration_username = request.user.username  # jishatech
            obj.ticket_username = client_registration_username
            obj.save()
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'ticket/bookTicket.html', {'form': form}, )