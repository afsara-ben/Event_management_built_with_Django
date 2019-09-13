from itertools import chain

from django.shortcuts import render
from django.views.generic import ListView
from agency.models import Agency, Agency_Info, AgencyBrief


class AdSearchView(ListView):
    template_name = 'search/view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            agency_results = Agency.objects.search(query=query)
            agency_info_results = Agency_Info.objects.search(query=query)
            agency_brief_results = AgencyBrief.objects.search(query=query)

            queryset_chain = chain(
                agency_results,
                agency_info_results,
                agency_brief_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=False)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Agency.objects.none()

