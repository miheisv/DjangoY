"""lyceum URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('about/', include('about.urls', namespace='about')),
    path('admin/', admin.site.urls),
]
