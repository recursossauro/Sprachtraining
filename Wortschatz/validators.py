from django.core.exceptions import ValidationError

def Bildgrosse(fl):
    if fl.size > 5242880:
        raise ValidationError('O tamaho máximo da imagem é 5MB')
    else:
        return fl
