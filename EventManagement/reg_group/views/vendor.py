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
                                  UpdateView)

from ..decorators import vendor_required
from ..forms import VendorSignUpForm
from ..models import User, User_Info


class VendorSignUpView(CreateView):
    model = User
    form_class = VendorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('vendor:vendor_profile')


@method_decorator([login_required, vendor_required], name='dispatch')
class QuizListView(ListView):
    model = User_Info
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'vendor_profile.html'

    def get_queryset(self):
        queryset = 'hello world is right vendor'
        return queryset


