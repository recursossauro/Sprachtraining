# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView # view do django.
from .views import IndexView, NeuerBenutzerView

urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('Einlass/', LoginView.as_view(template_name = 'Zugriff/Einlass.html'), name='login'),
    path('Ausgang/', LogoutView.as_view(next_page='index'), name='logout'),
    path('neuerBenutzer/', NeuerBenutzerView.as_view(), name='neuerBenutzer'),
]
