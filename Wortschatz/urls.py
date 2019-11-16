# -*- coding: utf-8 -*-

from django.urls import path

#from django.conf import settings

from .views import (
    IndexView,
    # Lander
    LanderlisteListView, NeuesLandCreateView, LandWechselnUpdateView, LandloschungDeleteView,
    # Sprachen
    SprachlisteListView, NeuesSpracheCreateView, SpracheWechselnUpdateView, SpracheloschenDeleteView,
    # Wortschatz
    BenutzervorgabenCreateView, BenutzervorgabenUpdateView, BenutzervorgabenDetailView,
    NeuesWortschatzCreateView, WortschatzDetailView, WortschatzListView, AndernWortschatzUpdateView, WortschatzloschenDeleteView,
    )

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    #Lander
    path('Landerliste/', LanderlisteListView.as_view(), name='Landerliste'),
    path('neuesLand/', NeuesLandCreateView.as_view(), name='neuesLand'),
    path('<slug:slug>/Landwechseln/', LandWechselnUpdateView.as_view(), name='Landwechseln'),
    path('<slug:slug>/LandLoschung/', LandloschungDeleteView.as_view(), name='LandLoschung'),
    # Sprachen
    path('Sprachliste/', SprachlisteListView.as_view(), name='Sprachliste'),
    path('neuesSprache/', NeuesSpracheCreateView.as_view(), name='neuesSprache'),
    path('<slug:slug>/Sprachewechseln/', SpracheWechselnUpdateView.as_view(), name='Sprachewechseln'),
    path('<slug:slug>/Spracheloschen/', SpracheloschenDeleteView.as_view(), name='Spracheloschen'),
    # Wortschatz
    path('neuesBenutzervorgaben/', BenutzervorgabenCreateView.as_view(), name='neuesBenutzervorgaben'),
    path('Benutzervorgabenechseln/', BenutzervorgabenUpdateView.as_view(), name='Benutzervorgabenechseln'),
    path('Benutzervorgaben/', BenutzervorgabenDetailView.as_view(), name='Benutzervorgaben'),
    #
    path('<int:pk>/Wortschatz/', WortschatzDetailView.as_view(), name='Wortschatz'),
    path('Vokabelliste/', WortschatzListView.as_view(), name='Vokabelliste'),
    path('neuesWortschatz/', NeuesWortschatzCreateView.as_view(), name='neuesWortschatz'),
    path('<int:pk>/andernWortschatz/', AndernWortschatzUpdateView.as_view(), name='andernWortschatz'),
    path('<int:pk>/Wortschatzloschen/', WortschatzloschenDeleteView.as_view(), name='Wortschatzloschen'),

]
