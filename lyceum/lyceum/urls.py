"""lyceum URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage', app_name='homepage')),
    path('catalog/', include('catalog.urls', namespace='catalog', app_name='catalog')),
    path('about/', include('about.urls', namespace='about', app_name='about')),
    path('admin/', admin.site.urls),
]
