from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from ..decorators import client_required
from ..forms import ClientSignUpForm
from ..models import User, User_Info


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('client:client_profile')


@method_decorator([login_required, client_required], name='dispatch')
class QuizListView(ListView):
    model = User_Info
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'client_profile.html'

    def get_queryset(self):
        queryset = 'hello world is good its client'
        return queryset


