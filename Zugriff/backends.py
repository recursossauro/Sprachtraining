# -*- coding: utf-8 -*-

from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model

class ModelBackend(BaseModelBackend):

    def authenticate(self, request, username=None, password=None):

        if not username is None:
            User = get_user_model() # Esta pode ser uma variável global, definida logo após os imports
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
