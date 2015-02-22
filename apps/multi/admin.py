# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Video, Ruta
from .forms import RutaForm
# Register your models here.
class RutaAdmin(admin.ModelAdmin):
    form = RutaForm
    list_display = ('titulo', 'especial')

admin.site.register(Video,)
admin.site.register(Ruta, RutaAdmin)
