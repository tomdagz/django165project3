from django.conf.urls import patterns, include, url
from .views import ContactView, VideoView

urlpatterns = patterns('',
  url(r'^$', ContactView.as_view(), name = 'contact'),
  url(r'^videos/$', VideoView.as_view(), name = 'video'),
)
