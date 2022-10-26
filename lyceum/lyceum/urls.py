"""lyceum URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', app_name='homepage')),
    path('catalog/', include('catalog.urls', app_name='catalog')),
    path('about/', include('about.urls', app_name='about')),
    path('admin/', admin.site.urls),
]
