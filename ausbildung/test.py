from Zugriff.models import User
from Wortschatz.models import Sprache
from ausbildung.models import Frage

def teste():
    eu = User.objects.get(username='leonardo')
    meu = Sprache.objects.get(name='Português brasileiro')
    alvo = Sprache.objects.get(name='Alemão')

    a = Frage.zufalligFragemitGewichten(eu, meu, alvo, 37)
    return a
