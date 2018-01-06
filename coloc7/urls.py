from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('comptes/', include('comptes.urls')),
    path('admin/', admin.site.urls),
    path('', include('lcl.urls')),
]
