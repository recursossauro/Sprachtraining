from django import forms

from .models import Antwort

class UbersetzenModelForm(forms.ModelForm):

    class Meta():
        model = Antwort
        fields = ['Antwort', 'Frage', 'begann']
        widgets = {
                'Frage': forms.HiddenInput,
                'begann': forms.HiddenInput,
            }
