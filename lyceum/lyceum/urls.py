"""lyceum URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage.urls')),
    path('catalog/', include('catalog.urls', namespace='catalog.urls')),
    path('about/', include('about.urls', namespace='about.urls')),
    path('admin/', admin.site.urls),
]
