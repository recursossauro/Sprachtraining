# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView # view do django.

urlpatterns = [

    path('Einlass/', LoginView.as_view(template_name = 'Zugriff/Einlass.html'), name='login'),
    path('Ausgang/', LogoutView.as_view(next_page='index'), name='logout'),
]
