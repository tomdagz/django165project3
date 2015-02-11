# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactoForm
# Create your views here.

class ContactView(FormView):

  template_name = 'contacto.html'
  form_class = ContactoForm
  success_url = '.'
