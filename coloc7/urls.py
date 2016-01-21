from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comptes/', include('comptes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('lcl.urls')),
]
