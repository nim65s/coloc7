from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comptes/', include('comptes.urls', namespace='comptes')),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),
    url(r'^admin/', include(admin.site.urls)),
)
