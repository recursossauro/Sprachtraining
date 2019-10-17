# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserAdminCreationForm

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'Zugriff/index.html'

class NeuerBenutzerView(CreateView):
    """ Eine View für die Registrierung neuer Benutzer. """
    form_class    = UserAdminCreationForm
    template_name =  'Zugriff/neuer_Benutzer.html'
    model         = get_user_model()
    success_url   = reverse_lazy('index')

class AndernBenutzerView(UpdateView):
    model = get_user_model()
    template_name = 'Zugriff/andern_Benutzer.html'
    fields = ['name', 'email']
    success_url   = reverse_lazy('Zugriff:index')

    def get_object(self):
        return self.request.user
