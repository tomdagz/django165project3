from django.conf.urls import patterns, include, url
from .views import ContactView

urlpatterns = patterns('',
  url(r'^$', ContactView.as_view(), name = 'contact'),
)
