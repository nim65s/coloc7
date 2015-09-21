from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comptes/', include('comptes.urls', namespace='comptes')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('lcl.urls', namespace='lcl')),
)
