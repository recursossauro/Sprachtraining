from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime
from random import randint, choices

# from Zugriff.models import User
#from django.contrib.auth import get_user_model

from Wortschatz.models import Wortschatz

#User = get_user_model()

class Frage(models.Model):

    FRAGETYP_OPTIONEN = (
        (0, 'Para o seu idioma'),
        (1, 'Para o idima estudado'),
    )

    Wortschatz    = models.ForeignKey(Wortschatz, verbose_name='Questão', on_delete=models.CASCADE, blank=True, null=True)
    Fragetyp      = models.IntegerField('Tipo de pergunta', default=FRAGETYP_OPTIONEN[0])
    Zufallsfaktor = models.IntegerField('Fator de aleatoriedade', default=5) # Varia de 1 a 10


    class Meta:
        unique_together = ('Wortschatz', 'Fragetyp')
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

    def getFrage(self):
        if self.Fragetyp == self.FRAGETYP_OPTIONEN[0][0]:
            return self.Wortschatz.wort + " em " + self.Wortschatz.sprache.name + " é:"
        else:
            return self.Wortschatz.ubersetzung + " em " + self.Wortschatz.sprachetraining.name + " é:"

    def FragenErstellen(Wortschatz):

        """
            Fragen Erstellen.
        ======================================================================
            Ziel: Erstellen Sie einige Fragen zum angegebenen Wort.
            Die Fragen lauten: schriftliche Übersetzung in Ihre Sprache
            und schriftliche Übersetzung in die gelernte Sprache.
        ----------------------------------------------------------------------

        """

        FrageTypNull = Frage(Wortschatz=Wortschatz, Fragetyp=Frage.FRAGETYP_OPTIONEN[0][0])
        FrageTypEin  = Frage(Wortschatz=Wortschatz, Fragetyp=Frage.FRAGETYP_OPTIONEN[1][0])

        FrageTypEin.save()
        FrageTypNull.save()

        return (FrageTypNull, FrageTypEin)


    def ErstellenalleFragen(user, sprache, sprachetraining):

        """
            Erstellen Sie alle Fragen.
        ======================================================================
            Ziel: Erstellen aller Paare schriftlicher Übersetzungsfragen
            basierend auf jedem Wort, sofern diese noch nicht vorhanden sind.
        ----------------------------------------------------------------------

        """

        Worte  = Wortschatz.objects.filter(user=user, sprache=sprache, sprachetraining = sprachetraining, frage__isnull=True)
        for Wort in Worte:
            Frage.FragenErstellen(Wort)

    def zufalligFrage(user, sprache, sprachetraining):

        #Refatorada - Não cria todas as perguntas para cada palavra, cria à medida que necessita.
        Worte = Wortschatz.objects.filter(user=user, sprache=sprache, sprachetraining = sprachetraining)
        AnzahlWorte = Worte.count()
        AnzahlFragetyp = len(Frage.FRAGETYP_OPTIONEN)

        # busca um número aleatório entre 0 e a quantidade total de possibilidades de perguntas.
        zufallig = randint(0, AnzahlWorte * AnzahlFragetyp - 1)
        Wort     = Worte[int(zufallig/AnzahlFragetyp)]
        Fragetyp = Frage.FRAGETYP_OPTIONEN[zufallig%AnzahlFragetyp][0]
        try:
            F = Frage.objects.get(Wortschatz=Wort, Fragetyp=Fragetyp)
        except: # DoesNotExist
            F = Frage(Wortschatz=Wort, Fragetyp=Fragetyp)
            F.save()

        return F

        """
            deprecated
            Cria uma pergunta para cada vocábulo, desde que já não exista.
            Retorna uma pergunta selecionada aleatóriamente.
        """
        #Frage.ErstellenalleFragen(user, sprache, sprachetraining)

        #fragen = Frage.objects.filter(Wortschatz__user=user, Wortschatz__sprache=sprache, Wortschatz__sprachetraining = sprachetraining)
        #i = randint(0, fragen.count()-1)
        #return fragen[i]

    def zufalligFragemitGewichten(user, sprache, sprachetraining, AnzahlFragen=10):

        AnzahlFragetyp              = len(Frage.FRAGETYP_OPTIONEN)
        WorteohneFragen             = Wortschatz.objects.filter(user=user, sprache=sprache, sprachetraining = sprachetraining, frage__isnull=True)
        Fragen                      = Frage.objects.filter(Wortschatz__user=user, Wortschatz__sprache=sprache, Wortschatz__sprachetraining = sprachetraining).order_by('Wortschatz')
        AnzahlWorte                 = WorteohneFragen.count()
        AnzahlFragen                = Fragen.count()

        Gewichten = []
        alleFragen_pk = []


        for Wort in WorteohneFragen:
            fen = Frage.FragenErstellen(Wort)
            for f in fen:
                alleFragen_pk.append(f.pk)
                Gewichten.append(f.Zufallsfaktor)
        f = None
        for frage in Fragen:
            alleFragen_pk.append(frage.pk)
            Gewichten.append(frage.Zufallsfaktor)
            if not f:
                f = frage
                Hilfs = [f.Fragetyp]
            elif f and f.Wortschatz == frage.Wortschatz:
                Hilfs += [frage.Fragetyp]
                f = frage
            else:
                # Verificar quais Fragetyp faltam comparando os conjuntos de frage.Wortschatz iguais;
                # Cria as Frages dos tipos que faltam;
                # Alimenta alleFragen e Gewindchten
                for typ in Frage.FRAGETYP_OPTIONEN:
                    if typ[0] not in Hilfs:
                        frage__ = Frage(frage.Wortschatz, typ[0])
                        frage__.save()
                        alleFragen_pk.append(frage__.pk)
                        Gewichten.append(frage__.Zufallsfaktor)
                # Reiniciar as variáveis
                f = frage
                Hilfs = [f.Fragetyp]

        return choices(alleFragen_pk,  weights=Gewichten, k=AnzahlFragen)

    def __str__(self):
        return self.getFrage()

class Antwort(models.Model):

    Frage     = models.ForeignKey(Frage, verbose_name='Questão', on_delete=models.CASCADE)
    begann    = models.DateTimeField('Começou as')
    bendet    = models.DateTimeField('Terminou as', auto_now_add=True)
    Fragetext = models.CharField('Texto da Resposta', max_length=1000)
    Antwort   = models.CharField('Resposta', max_length=200)

    # Campos para controle de backup
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def ist_richtig(self):
        if self.Frage.Fragetyp==Frage.FRAGETYP_OPTIONEN[0][0]:
            return self.Frage.Wortschatz.ubersetzung == self.Antwort
        else:
            return self.Frage.Wortschatz.wort == self.Antwort

    def Zeit(self):
        return (self.bendet - self.begann)

    def save(self, *args, **kwargs):

        self.Fragetext = self.Frage.getFrage()

        if self.ist_richtig():
            if (self.Frage.Zufallsfaktor>1):
                self.Frage.Zufallsfaktor -= 1
                self.Frage.save()
        else:
            if (self.Frage.Zufallsfaktor<10):
                self.Frage.Zufallsfaktor += 1
                self.Frage.save()

        super(Antwort, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ausbildung:ubersetzen', kwargs={'pk':self.pk})


    def __str__(self):
        return self.Antwort
