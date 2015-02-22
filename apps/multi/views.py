# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactoForm
from .models import Video
# Create your views here.

class ContactView(FormView):

  template_name = 'contacto.html'
  form_class = ContactoForm
  success_url = '.'

class VideoView(TemplateView):
    template_name = 'galeria.html'

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
