# -*- encoding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from .models import Ruta

class ContactoForm(forms.Form):
    # nombre_completo = forms.CharField(validators=[RegexValidator(regex=r'^\D+$', message = 'Introduzca sólo letras')],widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email           = forms.CharField(error_messages={'invalid':'Correo electrónico inválido: correo@ejemplo.com'},widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}))
    # telefono        = forms.CharField(label='Teléfono',validators=[RegexValidator(regex=r'^\d+$', message = 'Ingresa sólo dígitos numéricos')],required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # comentarios     = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
  nombre_completo = forms.CharField(label= _(u'Nombre'), validators=[RegexValidator(regex=r'^\D+$', message = _(u'Introduzca sólo letras'))],widget=forms.TextInput(attrs={'class': 'form-control'}))
  email           = forms.CharField(label= _(u'Correo'), error_messages={'invalid':_(u'Correo electrónico inválido: correo@ejemplo.com')},widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}))
  telefono        = forms.CharField(label= _(u'Teléfono'),validators=[RegexValidator(regex=r'^\d+$', message = _(u'Ingresa sólo dígitos numéricos'))],required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
  comentarios     = forms.CharField(label= _(u'Comentarios'), required=False,widget=forms.Textarea(attrs={'class':'form-control'}))

class RutaForm(forms.ModelForm):
    class Meta:
      model = Ruta

    def clean(self):

        cleaned_data = super(RutaForm, self).clean()
        obj_exist =  Ruta.objects.filter(especial=True).exclude(pk=self.instance.pk).first()
        if cleaned_data['especial'] == True and obj_exist:
            # import ipdb; ipdb.set_trace()
            self._errors['especial'] = self.error_class([u'¡Ya existe un especial :)!'])

        return cleaned_data
