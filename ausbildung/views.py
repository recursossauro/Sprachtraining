from django.shortcuts import render, get_object_or_404
from datetime import datetime

from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from .forms import UbersetzenModelForm
from .models import Antwort, Frage
from Wortschatz.models import Benutzervorgaben

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'ausbildung/index.html'

class UbersetzenCreateView(CreateView):

    form_class = UbersetzenModelForm
    template_name = 'ausbildung/Training_mit_zufalligen_Fragen.html'

    def get_initial(self):

        """
          1) Inicia a resposta com uma pergunta aleatória, de acordo com as preferências do usuário.
          2) Inicia o tempo para responder.
        """

        if not hasattr(self, 'Frage'):
            ben = get_object_or_404(Benutzervorgaben, user = self.request.user)
            self.Frage = Frage.zufalligFrage(user=ben.user, sprache = ben.sprache, sprachetraining = ben.sprachetraining)

        #self.begann = datetime.now()

        return {'Frage':self.Frage, 'begann':datetime.now()}

    def get_context_data(self, **kwargs):

        ctx = super(UbersetzenCreateView, self).get_context_data(**kwargs)
        ctx['Frage']   = self.Frage.getFrage()
        if self.kwargs.get('pk'):
            ctx['Antwort'] = Antwort.objects.get(pk=self.kwargs.get('pk'))

        return ctx

class AntwortenListView(ListView):

    template_name = 'ausbildung/Antworten.html'
    #model = Antwort

    def get_queryset(self):
        ben = get_object_or_404(Benutzervorgaben, user = self.request.user)
        return Antwort.objects.filter(
            Frage__Wortschatz__user = self.request.user,
            Frage__Wortschatz__sprache = ben.sprache,
            Frage__Wortschatz__sprachetraining = ben.sprachetraining
        ).order_by('-bendet')
