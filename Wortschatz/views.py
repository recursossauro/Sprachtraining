from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
  )

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings

from .models import Land, Sprache, Benutzervorgaben, Wortschatz

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'Wortschatz/index.html'

"""
      Lander
"""

class LanderlisteListView(LoginRequiredMixin, ListView):

    model = Land
    template_name = 'Wortschatz/Landerliste.html'

class NeuesLandCreateView(LoginRequiredMixin, CreateView):
    ""
    model = Land
    template_name = 'Wortschatz/neuesLand.html'
    fields = ['name', 'slug']

class LandWechselnUpdateView(LoginRequiredMixin, UpdateView):
    ""
    model = Land
    template_name = 'Wortschatz/neuesLand.html'
    fields = ['name', 'slug']

class LandloschungDeleteView(LoginRequiredMixin, DeleteView):
    model = Land
    template_name = 'Wortschatz/LandLoschungbestatigen.html'
    success_url = reverse_lazy('Wortschatz:Landerliste')

"""
    Sprachen
"""

class SprachlisteListView(LoginRequiredMixin, ListView):

    model = Sprache
    template_name = 'Wortschatz/Sprachliste.html'

class NeuesSpracheCreateView(LoginRequiredMixin, CreateView):

    model = Sprache
    template_name = 'Wortschatz/neuesSprache.html'
    fields = ['name', 'slug', 'lands']

class SpracheWechselnUpdateView(LoginRequiredMixin, UpdateView):

    model = Sprache
    template_name = 'Wortschatz/neuesSprache.html'
    fields = ['name', 'slug', 'lands']

class SpracheloschenDeleteView(LoginRequiredMixin, DeleteView):

    model = Sprache
    template_name = 'Wortschatz/SpracheLoschen.html'
    success_url = reverse_lazy('Wortschatz:Sprachliste')

"""
    Benutzervorgaben
"""

class BenutzervorgabenDetailView(LoginRequiredMixin, DetailView):

    model = Benutzervorgaben
    template_name = 'Wortschatz/Benutzervorgaben.html'
    fields = ['user', 'sprache', 'sprachetraining']

    def get_object(self):
        return Benutzervorgaben.objects.get(user=self.request.user)

class BenutzervorgabenCreateView(LoginRequiredMixin, CreateView):

    model = Benutzervorgaben
    template_name = 'Wortschatz/neuesBenutzervorgaben.html'
    fields = ['user', 'sprache', 'sprachetraining']

class BenutzervorgabenUpdateView(LoginRequiredMixin, UpdateView):

    model = Benutzervorgaben
    template_name = 'Wortschatz/neuesBenutzervorgaben.html'
    fields = ['sprache', 'sprachetraining']

    def get_object(self):
        try:
            benutzervorgaben = Benutzervorgaben.objects.get(user=self.request.user)
        except:
            benutzervorgaben = Benutzervorgaben(user=self.request.user)
            benutzervorgaben.save()

        return benutzervorgaben

"""
    Wortschatz
"""
class WortschatzDetailView(LoginRequiredMixin, DetailView):
    model = Wortschatz
    template_name = 'Wortschatz/Wortschatz.html'
    fields = ['sprache', 'sprachetraining', 'wort', 'ubersetzung', 'bild']

class WortschatzListView(LoginRequiredMixin, ListView):
    model = Wortschatz
    template_name = 'Wortschatz/Vokabelliste.html'
    fields = ['sprache', 'sprachetraining', 'wort', 'ubersetzung', 'bild']

class NeuesWortschatzCreateView(LoginRequiredMixin, CreateView):
    model         = Wortschatz
    template_name = 'Wortschatz/neuesWortschatz.html'
    fields = ['wort', 'ubersetzung', 'bild', 'sprache', 'sprachetraining']

    def get_initial(self):
        user = self.request.user
        """
            Consulta as preferências do usuário para pegar os idiomas de estudo e a conhecido.
        """
        try:
            benutzervorgaben = Benutzervorgaben.objects.get(user=user)
            return {'sprache':benutzervorgaben.sprache, 'sprachetraining': benutzervorgaben.sprachetraining}
        except:
            "Caso não tenha preferências executa com os idiomas nulos."
            return {'wort':user.username,}

    def form_valid(self, form):
        ""
        form.instance.user = self.request.user
        return super(NeuesWortschatzCreateView, self).form_valid(form)

class AndernWortschatzUpdateView(LoginRequiredMixin, UpdateView):
    model = Wortschatz
    template_name = 'Wortschatz/neuesWortschatz.html'
    fields = ['wort', 'ubersetzung', 'bild', 'sprache', 'sprachetraining']

class WortschatzloschenDeleteView(DeleteView):
    model = Wortschatz
    template_name = 'Wortschatz/Wortschatzloschen.html'
    success_url = reverse_lazy('Wortschatz:Vokabelliste')

class ZahltWorterTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'Wortschatz/zahltWorter.html'
