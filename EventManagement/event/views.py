from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.
from event.models import Event
from .forms import EventUpdateForm, EventCreate


# view for the index page
# class IndexView(generic.ListView):
# name of the object to be used in the index.html
#   context_object_name = 'event_list'
#  template_name = 'event/index.html'

# def get_queryset(self):
#     return Event.objects.all()


def ViewMyEvent(request):
    event_list = Event.objects.filter(event_username=request.user.username).all()
    if event_list:
        event_list_next = Event.objects.filter(event_username=request.user.username).order_by('-id')[0]
        sku = event_list_next.event_name
        return render(request, 'event/index.html', {'event_list': event_list, 'sku': sku})
    return render(request, 'event/index.html', {'event_list': event_list})

# view for the event entry page
# class EventEntry(CreateView):
#   model = Event
#  fields = ['event_name', 'event_venue', 'event_type']

# def __set__(self, instance, value):
#    instance.event_username = self.request.user.username


def EventEntry(request):
    if request.method == 'POST':
        form = EventCreate(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            event_registration_username = request.user.username  # jishatech
            obj.event_username = event_registration_username
            obj.save()
            form.save()
            return redirect('event:index')
    else:
        form = EventCreate()
    return render(request, 'event/event_form.html', {'form': form}, )


# view for the event update page
class EventUpdate(UpdateView):
    model = Event
    # the fields mentioned beindexlow become the entyr rows in the update form
    fields = ['event_name', 'event_venue', 'event_type']


def set_Event_Details(request, pk):
    if request.method == 'POST':
        obj = Event.objects.get(pk=pk)
        event_registration_username = request.user.username  # jishatech
        obj.event_username = event_registration_username
        if request.POST.get('name'):
            obj.event_name = request.POST.get('name')
        if request.POST.get('type'):
            obj.event_type = request.POST.get('type')
        if request.POST.get('venue'):
            obj.event_venue = request.POST.get('venue')
        if request.POST.get('budget'):
            obj.event_budget = request.POST.get('budget')
        if request.POST.get('date'):
            obj.event_date = request.POST.get('date')
        if request.POST.get('time'):
            obj.event_time = request.POST.get('time')
        if request.POST.get('size'):
            obj.event_size = request.POST.get('size')
        if request.POST.get('description'):
            obj.event_description = request.POST.get('description')
        obj.save()

        return redirect('event:index')
    return render(request, 'event/index.html')


def event_success(request):
    # value_ = Event.objects.filter(event_username=request.user.username).order_by('-id')[0]
    event = Event.objects.all();
    return render(request, 'show_details.html', {'event': event}, )


# view for deleting a event entry
class EventDelete(DeleteView):
    model = Event
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('event:index')


# def view_event_page(request, pk): # it's just passed as kwarg into view
#
#     details = Event.objects.get(pk=pk)
#     return render(request, 'event/event_page_details.html', {'details': details})

# def view_event_page(request): # it's just passed as kwarg into view
#     if request.method == 'GET':
#         sku = request.GET.get('sku')
#         if sku:
#             details = Event.objects.get(sku)
#             return render(request, 'event/event_page_details.html', {'details': details})
#         else:
#             # now you have the value of sku
#             # so you can continue with the rest
#            return render(request, 'event:index')


def view_event_page(request):
    if request.method == 'GET':
        sku = request.GET.get('sku')
        if sku:
            values = Event.objects.filter(event_name=sku).order_by('id')[0]
            return render(request, 'event/event_page_details.html', {'values': values})

