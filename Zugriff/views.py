# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserAdminCreationForm

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'Zugriff/index.html'

class NeuerBenutzerView(SuccessMessageMixin, CreateView):
    """ Eine View für die Registrierung neuer Benutzer. """
    form_class      = UserAdminCreationForm
    template_name   =  'Zugriff/neuer_Benutzer.html'
    model           = get_user_model()
    success_url     = reverse_lazy('index')
    success_message = 'Usuário criado com SUCESSO.'

class AndernBenutzerView(UpdateView):
    model = get_user_model()
    template_name = 'Zugriff/andern_Benutzer.html'
    fields = ['name', 'email']
    success_url   = reverse_lazy('Zugriff:index')

    def get_object(self):
        return self.request.user

class AndernPasswortView(LoginRequiredMixin, FormView):
    template_name = 'Zugriff/andern_Passwort.html'
    success_url = reverse_lazy('Zugriff:index')
    form_class = PasswordChangeForm

    def form_valid(self, form):
        form_valid = super(AndernPasswortView, self).form_valid(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(self.request, user)
        return form_valid

    def get_form_kwargs(self):
        kwargs = super(AndernPasswortView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
