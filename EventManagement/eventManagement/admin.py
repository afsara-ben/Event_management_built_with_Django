from django.contrib import admin
from transaction.models import AdminAgency_Transaction

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class eventManagementAdminSite(AdminSite):
    site_title = ugettext_lazy("admin site")

    site_header = ugettext_lazy("jisha admin")

    index_title = ugettext_lazy("jisha admin")


event_Management_Admin_Site = eventManagementAdminSite()

event_Management_Admin_Site.register(AdminAgency_Transaction)
