from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comptes/', include('comptes.urls', namespace='comptes')),
    url(r'^lcl/', include('lcl.urls', namespace='lcl')),
    url(r'^admin/', include(admin.site.urls)),
)
