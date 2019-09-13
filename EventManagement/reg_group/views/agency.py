from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)

from ..decorators import agency_required
from ..forms import AgencySignUpForm
from ..models import User, User_Info
from django.db.models import Q


class AgencySignUpView(CreateView):
    model = User
    form_class = AgencySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agency'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('agency:agency_profile')


@method_decorator([login_required, agency_required], name='dispatch')
class QuizListView(ListView):
    model = User_Info
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'agency_profile.html'

    def get_queryset(self):
        queryset = 'hello world is right'
        return queryset


class SearchResultsView(ListView):
    model = User
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(
            Q(username__icontains=query)
        )
        return object_list


@method_decorator([login_required, agency_required], name='dispatch')
class MapView(ListView):
    model = User_Info
    ordering = ('name',)
    context_object_name = 'map'
    template_name = 'google_map.html'

    def get_queryset(self):
        queryset = 'hello world is right'
        return queryset
