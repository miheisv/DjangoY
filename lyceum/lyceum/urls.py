"""lyceum URL Configuration"""

from os import abort
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
]
