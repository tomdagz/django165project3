# -*- encoding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Video(models.Model):

  class Meta:

    verbose_name = u'Video'
    verbose_name_plural = u'Videos'

  nombre = models.CharField(max_length=20)
  cover  = models.ImageField(upload_to='galeria/video/')
  url    = models.URLField(verbose_name=u'URL de Youtube',help_text=u'Ej. (https://www.youtube.com/watch/v=XXXXXXXXXX)',validators=[RegexValidator(regex = '^([\w\-]+)://(?:www).(?:youtube).([\w\-]+)/(?:watch).v=([\w\-]+)$', message = u'Ingrese una dirección válida de YouTube')])

  def __unicode__(self):
    return self.nombre

  def get_url_id(self):
    return self.url.split('=')[1]

class Ruta(models.Model):
    titulo   = models.CharField(u'Título',max_length=20,unique=True,help_text=u'Máximo 20 caracteres')
    especial = models.BooleanField()   
