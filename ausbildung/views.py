from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.urls import reverse_lazy

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

class UbersetzenCreateView(LoginRequiredMixin, CreateView):

    form_class = UbersetzenModelForm
    template_name = 'ausbildung/Training_mit_zufalligen_Fragen.html'

    def get_initial(self):

        """
          1) Inicia a resposta com uma pergunta aleatória, de acordo com as preferências do usuário.
          2) Inicia o tempo para responder.
        """

        if not hasattr(self, 'Frage'):
            ben = get_object_or_404(Benutzervorgaben, user = self.request.user)
            _Frage = Frage.zufalligFrage(user=ben.user, sprache = ben.sprache, sprachetraining = ben.sprachetraining)

        #self.begann = datetime.now()

        return {'Frage':self.Frage, 'begann':datetime.now()}

    def get_context_data(self, **kwargs):

        ctx = super(UbersetzenCreateView, self).get_context_data(**kwargs)
        ctx['Frage']   = self.Frage.getFrage()
        if self.kwargs.get('pk'):
            ctx['Antwort'] = Antwort.objects.get(pk=self.kwargs.get('pk'))

        return ctx

class PrufungCreateView(LoginRequiredMixin, CreateView):

    template_name = 'ausbildung/Prufung.html'
    form_class    = UbersetzenModelForm
    success_url   = reverse_lazy('ausbildung:Prufung')


    def get_initial(self):

        Fragen = ''

        if 'Fragen' in self.request.session:
            Fragen = self.request.session["Fragen"]

        if not Fragen or len(Fragen)==0:
            ben = get_object_or_404(Benutzervorgaben, user = self.request.user)
            Fragen = Frage.zufalligFragemitGewichten(user=ben.user, sprache = ben.sprache, sprachetraining = ben.sprachetraining, AnzahlFragen=10)
            self.request.session['Fragen'] = Fragen


        self.Frage = Frage.objects.get(pk=Fragen[0])



        # Inicia o tempo para responder.
        # Inicia a Pergunta.
        return {'Frage':self.Frage, 'begann':datetime.now()}


    def get_context_data(self, **kwargs):
        """
          1) Vefifica se tem sequencia de perguntas selecionadas, caso contrário, cria a sequencia.
          2) Inicia a resposta com uma pergunta aleatória, de acordo com as preferências do usuário.
        """

        ctx = super(PrufungCreateView, self).get_context_data(**kwargs)
        ctx['Frage']  = self.Frage.getFrage()
        if self.kwargs.get('pk'):
            ctx['Antwort'] = Antwort.objects.get(pk=self.kwargs.get('pk'))

        return ctx

    def get_success_url(self, **kwargs):

        self.request.session["Fragen"] = self.request.session["Fragen"][1:]

        return reverse_lazy('ausbildung:Prufung', kwargs={'pk': self.object.pk})

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
