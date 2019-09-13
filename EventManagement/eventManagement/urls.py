"""eventManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .admin import event_Management_Admin_Site
from django.urls import path, include
from reg_group.views import client, agency, reg_group, vendor
from requestBrief.views import popup, request_view, servicerequest_view, servicerequest_success, servicematch, servicematch_success_showlittle
from requestBrief.views import servicematch_success, servicematch_message
from requestBrief.views import request_success, match, match_success, client_request_history, match_message , agencyclient_message
from relation.views import AdSearchView
from agency.views import agency_vendor_success, agency_message, agencylist_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from tickets.views import ViewTicket, TicketEntry

admin.site.site_header = "jisha"
admin.site.site_title = "jisha"
admin.site.index_title = "jisha"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', event_Management_Admin_Site.urls),
    path('', include('reg_group.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', reg_group.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/', client.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/agency/', agency.AgencySignUpView.as_view(), name='agency_signup'),
    path('accounts/signup/vendor/', vendor.VendorSignUpView.as_view(), name='vendor_signup'),

    path('search/', agency.SearchResultsView.as_view(), name='search_results'),

    path('client/myrequest/', request_view, name='popup'),
    path('client/agencylist', agencylist_view, name='agencylistview'),
    path('client/myservicerequest/', servicerequest_view, name='servicepopup'),
    path('client/myBrief/', request_success, name='createBrief'),
    path('client/myserviceBrief/', servicerequest_success, name='servicecreateBrief'),
    path('client/mymatch/', match, name='mymatch'),
    path('client/myservicematch/', servicematch, name='myservicematch'),
    path('client/history/', client_request_history, name='client_request_history'),
    path('client/mymatch/agency/', match_success, name='agency_match'),

    path('agency/vendor/', agency_vendor_success, name='agency_vendor_match'),

    path('client/myservicematch/vendor/', servicematch_success, name='vendor_match'),
    path('client/myservicematch/', servicematch_success_showlittle, name='vendor_match_little'),
    path('client/mymatch/agency/message', match_message, name='agency_message'),
    path('client/myservicematch/vendor/message', servicematch_message, name='vendor_message'),
    path('agency/profile/preference/message', agency_message, name='agency_reply_message'),
    path('client/mymatch/agencyclient/message', agencyclient_message, name='agencyclient_message'),

    path('agency/search/', AdSearchView.as_view(), name='search'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('feedback/', include('feedback.urls')),

    url(r'^ticket/', TicketEntry, name='view_ticket'),
    url(r'^event/', include('event.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
