from django.urls import path
from django.conf.urls import url

from event import views
from .views import set_Event_Details, event_success, ViewMyEvent, view_event_page, EventEntry  # view_event_page

app_name = 'event'

urlpatterns = [

    # /event/
    url(r'^$', ViewMyEvent, name='index'),

    # event/event/entry
    url('entry/$', EventEntry, name='event-entry'),

    # event/product/2
    url(r'^(?P<pk>[0-9]+)/$', views.EventUpdate.as_view(), name='event-update'),

    url(r'^(?P<pk>[0-9]+)/update$', set_Event_Details, name='event_details'),

    url('success/$', event_success, name='Allevents'),
    # url('details/$', view_event_page, name='viewEventPage'),
    # url(r'^(?P<pk>[0-9]+)/details$', view_event_page, name='details'),
    # url(r'^details/eventDetail-(?P<parameter>[\w-]+).html', view_event_page, name="viewEventPage"),

    # url(r'^(?P<pk>[0-9]+)/$', views.EventAdvancedUpdate.as_view(), name='event-advanced-update'),

    # event/product/(?P<pk>[0-9]+)/delete
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.EventDelete.as_view(), name='event-delete'),
    # path('', reg_group.home, name='home'),
    # url(r'^(?P<pk>\d+)/$', view_event_page, name='details'),
    url(r'^detail/$', view_event_page, name="details"),

]
