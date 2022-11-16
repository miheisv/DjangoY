"""lyceum URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('about/', include('about.urls', namespace='about')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
