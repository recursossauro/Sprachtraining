# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from .forms import UserAdminCreationForm

class NeuerBenutzerView(CreateView):
    """ Eine View für die Registrierung neuer Benutzer. """
    form_class    = UserAdminCreationForm
    template_name =  'Zugriff/neuer_Benutzer.html'
    model         = get_user_model()
    success_url   = reverse_lazy('index')
