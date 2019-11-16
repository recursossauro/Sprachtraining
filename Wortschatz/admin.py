from django.contrib import admin

from .models import Land, Sprache, Land_Sprache

admin.site.register(Land)
admin.site.register(Sprache)
admin.site.register(Land_Sprache)
