# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.conf import settings

# from Zugriff.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

class Land(models.Model):
    name = models.CharField('Nome', max_length = 100, unique=True)
    slug = models.SlugField('Abreviatura', max_length = 4, unique=True)

    created = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modificado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['name', 'slug', 'created', 'modified']

    def get_absolute_url(self):
        return reverse('Wortschatz:Landerliste')

    def __str__(self):
        return self.slug + ' - ' + self.name

class Sprache(models.Model):
    name  = models.CharField('Nome', max_length = 100, unique=True)
    slug  = models.SlugField('Abreviatura', max_length = 7, unique=True)
    lands = models.ManyToManyField(Land, through='Land_Sprache', verbose_name="Países")

    created = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modificado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['name', 'slug', 'created', 'modified']

    def get_absolute_url(self):
        return reverse('Wortschatz:Sprachliste')

    def __str__(self):
        return self.name + '(' + self.slug + ')'

class Land_Sprache(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    sprache = models.ForeignKey(Sprache, on_delete=models.CASCADE)
    amtssprache = models.BooleanField('Língua Oficial', default = True)

    created = models.DateTimeField('Criado em', auto_now_add=True, null=True)
    modified = models.DateTimeField('Modificado em', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Idioma de País'
        verbose_name_plural = 'Idiomas de Países'
        ordering = ['land', 'sprache', 'amtssprache', 'created', 'modified']

    def get_absolute_url(self):
        return reverse_lazy('Wortschatz:Sprachlist')

    def __str__(self):
        return self.land.slug + ' - ' + self.sprache.slug

class Benutzervorgaben(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'Usuário', on_delete=models.CASCADE, unique=True)
    sprache         = models.ForeignKey(Sprache, verbose_name = 'Idioma compreendido', on_delete=models.CASCADE, blank=True, null=True)
    sprachetraining = models.ForeignKey(Sprache, related_name = 'sprachetraining_standard', verbose_name = 'Idioma de treino', on_delete=models.CASCADE, blank=True, null=True)
    # Campos para controle de backup
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Preferência'
        verbose_name_plural = 'Preferências'

    def get_absolute_url(self):
        return reverse('Wortschatz:Benutzervorgaben')

    def __str__(self):
        return str(self.user)

class Wortschatz(models.Model):

    sprache         = models.ForeignKey(Sprache, verbose_name = 'Idioma compreendido', on_delete=models.CASCADE)
    sprachetraining = models.ForeignKey(Sprache, related_name = 'sprachetraining', verbose_name = 'Idioma de treino', on_delete=models.CASCADE)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE)
    ubersetzung     = models.CharField('Tradução', max_length=200, null=True, blank=True)
    wort            = models.CharField('Palavra', max_length=200, null=True, blank=True)
    bild            = models.ImageField('Imagem', upload_to='Benutzer/', max_length=500, null=True, blank=True)

    # Campos para controle de backup
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        unique_together = ('user', 'sprache', 'sprachetraining', 'ubersetzung', 'wort')
        verbose_name    = 'Vocabulário'
        verbose_name_plural = 'Vocabulários'

    def get_absolute_url(self):
        return reverse('Wortschatz:Wortschatz', kwargs={'pk':self.pk})

    def __str__(self):
        return self.wort

"""
    Classe n para n Classe de vocabulário
    O primeiro vocabulário é a Classe.
    O segundo vocabulário pertence àquela Classe
"""
